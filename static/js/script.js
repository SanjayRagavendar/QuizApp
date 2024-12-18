document.querySelector("form").addEventListener("submit", function(e) {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    if (!username || !password) {
        alert("Please fill out all fields.");
        e.preventDefault();
    }
});
