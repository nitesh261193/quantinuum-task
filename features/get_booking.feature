Feature: Get Booking Details
  As a user of the booking system
  I want to retrieve booking details
  So that I can verify reservation information

  Background:
    Given The system is ready to interact with user
    Given I have created username_password header 'universal_header'

  Scenario: Create and retrieve a booking
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
      "additionalneeds": "Breakfast"
    }
    """
    # First create a booking
    When I create a booking with the following details
      | field                 | value               |
      | headers               | #{universal_header} |
      | body                  | #{booking_payload}  |
      | response_to_be_stored | post_booking        |
      | booking_id_stored_as  | booking_id          |
    Then I see status code '200' in '#{post_booking}'
    # Now get the booking details
    When I send GET request for booking
      | field                 | value               |
      | headers               | #{universal_header} |
      | booking_id            | #{booking_id}       |
      | response_to_be_stored | get_booking         |
    Then I see status code '200' in '#{get_booking}'
    Then the json path in '#{get_booking}' has specific value in the object
      | json_path               | expected_value |
      | $.firstname             | Jim            |
      | $.lastname              | Brown          |
      | $.totalprice            | 111            |
      | $.depositpaid           | True           |
      | $.bookingdates.checkin  | 2018-01-01     |
      | $.bookingdates.checkout | 2019-01-01     |
      | $.additionalneeds       | Breakfast      |

  Scenario: Retrieve booking ids
    When I send GET request for all booking ids
      | field                 | value               |
      | headers               | #{universal_header} |
      | response_to_be_stored | get_booking_ids     |
    Then I see status code '200' in '#{get_booking_ids}'
    Then the json path in '#{get_booking_ids}' has specific value in the object
      | json_path      | expected_value |
      | $[0].bookingid | 928            |
