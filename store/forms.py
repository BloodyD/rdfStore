from django import forms

class LoadForm(forms.Form):
  rdf_content = forms.CharField(
    label="RDF content", 
    widget=forms.Textarea(attrs={
      'rows':15, 
      'placeholder':"Enter valid RDF content here",
      "class":"form-control",
      "id":"rdf-content",
    })
  )
  load_type = forms.Field(
    widget=forms.HiddenInput(attrs={
      "id":"load-type",
      "value":"n3"
      })
  )


class QueryForm(forms.Form):
  rdf_query = forms.CharField(
    label="SPARQL query", 
    widget=forms.Textarea(attrs={
      'rows':15, 
      'placeholder':"Enter valid SPARQL query here",
      "class":"form-control",
      "id":"rdf-query",
    })
  )
  output_type = forms.Field(
    widget=forms.HiddenInput(attrs={
      "id":"output-type",
      "value":"xml"
      })
  )

