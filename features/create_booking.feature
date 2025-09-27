Feature: Booking Creation

  Background:
    Given The system is ready to interact with user
    Given I have created username_password header 'universal_header'


  Scenario: Create a new booking
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
    Then the json path in '#{post_booking}' has specific value in the object
      | json_path                       | expected_value |
      | $.bookingid                     | #{booking_id}  |
      | $.booking.firstname             | Jim            |
      | $.booking.lastname              | Brown          |
      | $.booking.totalprice            | 111            |
      | $.booking.depositpaid           | True           |
      | $.booking.bookingdates.checkin  | 2018-01-01     |
      | $.booking.bookingdates.checkout | 2019-01-01     |
      | $.booking.additionalneeds       | Breakfast      |


