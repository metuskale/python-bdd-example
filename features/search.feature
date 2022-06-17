# -- FILE: features/search.feature
Feature: DuckDuckGoAPI

  Scenario Outline: Word search
    Given the <endpoint> and the search string <string_to_search>
    When we perform the search
    Then the source of the result is <source_result>
    And the URL of the result is <url_result>

    Examples:
      | endpoint                    | string_to_search | source_result | url_result                           |
      | https://api.duckduckgo.com/ | Toledo           | Wikipedia     | https://en.wikipedia.org/wiki/Toledo |