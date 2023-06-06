// form-validation.js

// Function to validate the form
function validateForm() {
    // Get the form element
    var form = document.getElementById("login_form");
  
    // Get the input values
    var name = form.elements["student_name"].value;
    var regNo = form.elements["reg_no"].value;
    var phoneNo = form.elements["phone_no"].value;
    var email = form.elements["email"].value;
    var department = form.elements["department"].value;
    var address = form.elements["address"].value;
    var leavingDate = form.elements["leaving_date"].value;
    var arrivingDate = form.elements["arriving_date"].value;
    var leavingTime = form.elements["leaving_time"].value;
    var arrivingTime = form.elements["arriving_time"].value;
  
    // Perform validation
    if (name === "") {
      alert("Please enter your name.");
      return false;
    }
    if (regNo === "") {
      alert("Please enter your registration number.");
      return false;
    }
    if (phoneNo === "") {
      alert("Please enter your phone number.");
      return false;
    }
    if (email === "") {
      alert("Please enter your email address.");
      return false;
    }
    if (department === "") {
      alert("Please select your department.");
      return false;
    }
    if (address === "") {
      alert("Please enter your address.");
      return false;
    }
    if (leavingDate === "") {
      alert("Please enter the date of leaving.");
      return false;
    }
    if (arrivingDate === "") {
      alert("Please enter the date of arriving.");
      return false;
    }
    if (leavingTime === "") {
        alert("Please enter the date of leaving.");
        return false;
    }
    if (arrivingTime === "") {
        alert("Please enter the date of arriving.");
        return false;
    }
  
    // Form is valid, submit the form
    return true;
  }
  