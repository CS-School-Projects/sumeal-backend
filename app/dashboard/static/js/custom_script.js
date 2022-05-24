// Form validation
window.addEventListener('load', function () {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function (form) {
        form.addEventListener('submit', function (event) {
            if (form.checkValidity() === false) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
})


// Deletion
const confirmationForms = document.querySelectorAll(".requires-confirmation")
confirmationForms?.forEach(form => {
    const message = form.dataset.message
    form.addEventListener("submit", event => {
        response = confirm(message)
        if (!response) {
            event.preventDefault()
        }
    })
})

