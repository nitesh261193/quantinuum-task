Feature: Booking Patch Update

  Background:
    Given The system is ready to interact with user
    Given I have created username_password header 'universal_headers'
    Given I have created token header 'token_header'


  Scenario: Create and update the booking partially
    Given The payload stored as 'booking_payload'
    """
    {
      "firstname": "Jim",
      "lastname": "Brown",
      "totalprice": 111,
      "depositpaid": true,
      "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
      },
      "additionalneeds": "Dinner"
    }
    """
    When I create a booking with the following details
      | field                 | value                |
      | headers               | #{universal_headers} |
      | body                  | #{booking_payload}   |
      | response_to_be_stored | post_booking         |
      | booking_id_stored_as  | booking_id           |
    Then I see status code '200' in '#{post_booking}'
    Given The payload stored as 'booking_payload_updated'
    """
    {
      "firstname" : "James",
      "lastname" : "Brown"
    }
    """
    When I update partial booking with the following details
      | field                 | value                      |
      | headers               | #{token_header}            |
      | body                  | #{booking_payload_updated} |
      | booking_id            | #{booking_id}              |
      | response_to_be_stored | update_partial_booking     |
    Then I see status code '200' in '#{update_partial_booking}'
    Then the json path in '#{update_partial_booking}' has specific value in the object
      | json_path               | expected_value |
      | $.firstname             | James          |
      | $.lastname              | Brown          |
      | $.totalprice            | 111            |
      | $.depositpaid           | True           |
      | $.bookingdates.checkin  | 2018-01-01     |
      | $.bookingdates.checkout | 2019-01-01     |
      | $.additionalneeds       | Dinner         |



