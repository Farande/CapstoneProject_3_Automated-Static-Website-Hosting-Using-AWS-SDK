function adjustAssetPaths() {
    const heroImage = document.querySelector(".showcase-card img");
    if (!heroImage) return;

    const isNestedPreview = window.location.pathname.includes("/website/");
    heroImage.src = isNestedPreview
        ? "../images/hero-illustration.svg"
        : "images/hero-illustration.svg";
}

function showMessage() {
    const messages = [
        "Website deployed successfully using Python + boto3!",
        "Your S3 static website is live and optimized for performance.",
        "Cloud deployment complete — everything is ready to serve traffic."
    ];

    const messageBox = document.getElementById("message");
    const randomMessage = messages[Math.floor(Math.random() * messages.length)];

    if (messageBox) {
        messageBox.textContent = randomMessage;
    }
}

document.addEventListener("DOMContentLoaded", adjustAssetPaths);