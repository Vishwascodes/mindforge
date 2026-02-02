document.addEventListener("DOMContentLoaded", () => {
  const username = localStorage.getItem("username") || "guest";
  const scoreEl = document.getElementById("score");

  // Fetch user score from backend
  fetch("http://127.0.0.1:5000/get-score?username=" + username)
    .then((res) => res.json())
    .then((data) => {
      if (data.score !== undefined) {
        scoreEl.textContent = data.score;
      } else {
        scoreEl.textContent = 0;
      }
    });

  // Navigate to game page
  document.getElementById("startGameBtn").addEventListener("click", () => {
    window.location.href = "/game";
  });
});
