from django import template
import simplejson as json
import xml.etree.ElementTree as ET

register = template.Library()

def parseXml(content):
  content = content.replace("sparql:", "")
  doc = ET.fromstring(content)

  heads = [head.attrib.get("name") for head in doc.findall(".//head/variable")]

  values = []
  for res in doc.findall(".//results/result"):
    values.append([res.find("*[@name='%s']/" %(head)).text for head in heads])
    
  return {
    "heads": heads,
    "values": values
  }

def parseJson(content):
  contDict = json.loads(content)
  heads = contDict.get("head", {}).get("vars", [])
  rawValues = contDict.get("results", {}).get("bindings", [])
  values = []
  for rawVal in rawValues:
    newValue = [rawVal.get(head, {}).get("value") for head in heads]
    values.append(newValue)
  return {"heads": heads, "values": values}

@register.inclusion_tag('inclusions/result_table.html')
def show_result(content, format):
  result = {}
  if format=="xml":
    result.update(parseXml(content))
  elif format=="json":
    result.update(parseJson(content))

  # result.update()
  return result