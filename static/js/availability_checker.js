// This code runs when the document is ready
$(document).ready(function () {
    let isAvailable = true;

    // When the date or time input fields change
    $('#id_date, #id_time').change(function () {
        // Gets the selected date and time values
        let date = $('#id_date').val();
        let time = $('#id_time').val();

        // Check if both date and time are selected
        if (date && time) {
            // Sends request to check availabilty
            $.get('/check_availability/', { date: date, time: time }, function (data) {
                // If available
                if (data.available) {
                    // Tell user time is available
                    alert('Date and Time are available!');
                    // Update the availability status
                    isAvailable = true;
                    // Enable the submit button
                    $('form button[type="submit"]').prop('disabled', false);
                } else {
                    // Tell user not available
                    alert('Date and Time are not available.');
                    // Update the availability status
                    isAvailable = false;
                    // Disable the submit button
                    $('form button[type="submit"]').prop('disabled', true);
                }
            });
        }
    });

    // When the form is submitted
    $('form').submit(function (e) {
        // If the date and time are not available
        if (!isAvailable) {
            // Prevent the form submission
            e.preventDefault();
            // Ask user to choose different time and date
            alert('Please choose a different date or time.');
        }
    });
});