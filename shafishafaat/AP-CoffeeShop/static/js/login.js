document.addEventListener("DOMContentLoaded", function() {
    const signupForm = document.querySelector(".signup-form");
    const loginForm = document.querySelector(".login-form");

    if (signupForm) {
        signupForm.addEventListener("submit", function(event) {
            const password = signupForm.querySelector("#password").value;
            if (password.length < 6) {
                event.preventDefault();
                alert("رمز عبور باید حداقل 6 کاراکتر باشد.");
            }
        });
    }

    if (loginForm) {
        loginForm.addEventListener("submit", function(event) {
            const username = loginForm.querySelector("#username").value;
            const password = loginForm.querySelector("#password").value;
            if (!username || !password) {
                event.preventDefault();
                alert("نام کاربری و رمز عبور نباید خالی باشند.");
            }
        });
    }
});
