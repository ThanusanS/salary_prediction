function predict() {
  const years = document.getElementById("years").value;

  fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      years: years,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.prediction) {
        document.getElementById("result").innerText =
          "Predicted Salary: " + data.prediction;
      } else {
        document.getElementById("result").innerText =
          "Server Error: " + data.error;
      }
    })
    .catch((error) => {
      console.log(error);
      document.getElementById("result").innerText = "Error occurred!";
    });
}
