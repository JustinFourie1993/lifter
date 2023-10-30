# Tables

Tables is a robust and user-friendly restaurant booking system designed to streamline the reservation process for both restaurant owner and customer. This web app provides an elegant solution for managing table reservations, enabling customers to book their preferred dining times and allowing restaurant staff to efficiently organize and confirm bookings.

# Features

## Home page

* The user is met by a warm homepage with ifromation about the restuarant and staff.
* The navigation bar helps users move seamlessly from page to page.

![](readme-images/home-page.png)

## Real-time Availability

* The system provides real-time availability updates, ensuring that customers recieve accurate information on table availability.

## Customizable Menus

* The restaurant can showcase and edit thier menus, including detailed descriptions and prices.

![](readme-images/menu.png)

## User Profiles

* Diners can create and manage their profiles, making it easy to view and modify their reservations.


## Admin Dashboard

* Restaurant owner and staff have access to a powerful admin dashboard for managing reservations and updating menus.

## Responsive Design

* The application is designed to be fully responsive, providing a seamless booking experience on both desktop and mobile devices.

![](readme-images/responsive.png)

## Cloud integration

* Images and media assets are seamlessly integrated with Cloudinary, insuring efficient storage and retrieval of media content.

# Testing

* Automated python test were carried out for forms.py, models.py and views.py using Testcase.
* Tests can be found in respective test_forms.py, test_models.py and test_views.py.

* I have tested the web app manually both locally and after deployment
  
#### List of manual tests carried out that revealed app works as intended

* User registration - Verified that users can successfully create new accounts with valid information by creating multiple users.
* Login - Confirmed that created users can login by using those credentials to login.
* Booking creation - Successfully created multiple bookings(only when logged in) that were then displayed in booking.html.
* Booking confirmation - Once a booking was made i recieved an alert message telling me the booking was successful.
* Booking Modification - Apon creating a booking, a was able to edit both time, date and number of guests(only when logged in).
* Cancellation - In addition to editing i was able to delete any bookings(only when logged in).
* Reservation Management - while logged in as an admin i could view, modify and cancel any bookings.
* Menu Display - I tested adding and removing meal objects as an admin and respectively those meal were added/rmoved and displayed as such in the menu.html.
* Mobile Compatibility - Tested the app's responsiveness on various screen sizes (desktop, tablet, and smartphone) to ensure a consistent user experience.
* 

## Validator Testing

* HTML
  * No errors were returned when passing through the official [W3C Validator](https://validator.w3.org/#validate_by_input)

* Css
  * No errors were returned when passing through the official [(Jigsaw) Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

* Javascript
  * No errors were returned when passing through the [(JShint) Validator](https://jshint.com/), just 3  warnings.


# Planning
## Project Objectives

* Enhance Dining Experience: My goal is to create a user-friendly platform that simplifies the reservation process for customers, making it convenient to book a table at their favorite restaurant.
* Restaurant Efficiency: I aim to improve restaurant operations by providing an efficient reservation management system for restaurant owners and staff.
### Planning highlights
* User-Centric Approach: I started by identifying the needs of both restaurant owners and diners. This user-centric approach guided My feature selection and design choices.
* Requirements: Requirements were gathered, including user stories, wich exist in a canban board connected to the [github repo](https://github.com/users/JustinFourie1993/projects/5).

## Design
* Wireframes - I created wireframes of what i wanted the web app to look like.

![](readme-images/Home-wireframe.png)
![](readme-images/Menu-wireframe.png)

# Deployment



Live link - []()

# Credits

## Content

 

## Media

