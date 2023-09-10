document.addEventListener('DOMContentLoaded', function () {
    const lengthInput = document.getElementById('length');
    const generateButton = document.getElementById('generate');
    const passwordDisplay = document.getElementById('password-display');

    generateButton.addEventListener('click', generatePassword);

    function generatePassword() {
        const length = lengthInput.value;
        const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:<>,.?/";
        let password = "";

        for (let i = 0; i < length; i++) {
            const randomIndex = Math.floor(Math.random() * charset.length);
            password += charset.charAt(randomIndex);
        }

        passwordDisplay.textContent = `Your generated password: ${password}`;
    }
});