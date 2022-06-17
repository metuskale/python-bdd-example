# -- FILE: features/steps/search_steps.py
from behave import when, then, given

import common
import requests

@given(u'the {endpoint} and the search string {string_to_search}')
def step_impl(context, endpoint, string_to_search):
    assert endpoint is not None
    assert string_to_search is not None
    assert len(string_to_search) > 0

    URL = endpoint + common.API_URL_QUERY.replace("{{QUERY}}", string_to_search)
    context.URL = URL

@when(u'we perform the search')
def step_impl(context):
    response = requests.get(context.URL)
    assert response.status_code == 200

    # pass response for check in next step
    context.response = response

@then(u'the source of the result is {source_result}')
def step_impl(context, source_result):
    response_json = context.response.json()
    assert response_json['AbstractSource'] == source_result

@then(u'the URL of the result is {url_result}')
def step_impl(context, url_result):
    response_json = context.response.json()
    assert response_json['AbstractURL'] == url_result