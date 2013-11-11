from django import template
import simplejson as json

register = template.Library()

def parseXml(content):
  return {
    "heads":["1", "2"],
    "values": [
      ["a", "b"],
      ["a", "b"],
      ["a", "b"],
      ["a", "b"],
      ["a", "b"],
      ["a", "b"],
    ]
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