Feature: Booking Deletion


  Background:
    Given The system is ready to interact with user
    Given I have created username_password header 'universal_headers'
    Given I have created token header 'token_headers'


  @delete_call
  Scenario: Create a new booking and delete it
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
    When I create a booking with the following details
      | field                 | value                |
      | headers               | #{universal_headers} |
      | body                  | #{booking_payload}   |
      | response_to_be_stored | post_booking         |
      | booking_id_stored_as  | booking_id           |
    Then I see status code '200' in '#{post_booking}'
    When I send request to delete booking
      | field                 | value            |
      | headers               | #{token_headers} |
      | booking_id            | #{booking_id}    |
      | response_to_be_stored | delete_booking   |
    Then I see status code '201' in '#{delete_booking}'


