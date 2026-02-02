fetch("http://127.0.0.1:5000/get-question")
  .then(res => res.json())
  .then(data => {
    document.getElementById("question").innerText = data.question;

    data.options.forEach(opt => {
      let btn = document.createElement("button");
      btn.innerText = opt;
      btn.onclick = () => checkAnswer(opt, data.answer);
      document.getElementById("options").appendChild(btn);
    });
  });

function checkAnswer(selected, correct) {
  if (selected === correct) {
    alert("Correct! Level Up 🚀");
  } else {
    alert("Wrong ❌");
  }
}
