from django import forms
from django.conf import settings
import requests

class DictionaryForm(forms.Form):
    word = forms.CharField(max_length=100)

    def search(self):
        result = {}
        word = self.cleaned_data['word']
        endpoint = 'https://od-api.oxforddictionaries.com/api/v2/entries/{source_lang}/{word_id}'
        url = endpoint.format(source_lang='en', word_id=word)
        headers = {'app_id': settings.OXFORD_APP_ID, 'app_key': settings.OXFORD_APP_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found for "%s"' % word
            else:
                result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
        return result

class GithubJobForm(forms.Form):
    description = forms.CharField()
    location = forms.CharField()
    full_time = forms.BooleanField()

    def search_job(self):
        result = {}
        description = self.cleaned_data['description']
        location = self.cleaned_data['location']
        full_time = str(self.cleaned_data['full_time'])
        url = "https://jobs.github.com/positions.json?description=" + description.lower()
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            result['search_result'] = data
            result['success'] = True

        else:
            result['success'] = False
            if response.status_code == 404:
                result['message'] = 'No jobs found for %s' % description

            else:
                result['message'] == 'The Github API is not available'

        return result
