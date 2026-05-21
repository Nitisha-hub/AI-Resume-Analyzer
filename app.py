<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>AI Career & Resume Analyzer</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Poppins', sans-serif;
      background: #f0f4f8;
      color: #333;
      padding: 30px;
    }

    .container {
      max-width: 900px;
      margin: auto;
      background: #fff;
      padding: 30px;
      border-radius: 15px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
      color: #2c3e50;
    }

    input[type="file"] {
      padding: 10px;
      margin-top: 15px;
    }

    button {
      background: #3498db;
      color: white;
      padding: 12px 25px;
      margin-top: 10px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-weight: bold;
      transition: 0.3s;
    }

    button:hover {
      background: #2980b9;
    }

    #result {
      display: none;
      margin-top: 30px;
    }

    .section {
      margin-top: 20px;
      padding: 20px;
      border-left: 5px solid #3498db;
      background: #f9f9f9;
      border-radius: 10px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
    }

    th, td {
      padding: 12px;
      border-bottom: 1px solid #ccc;
    }

    th {
      background-color: #3498db;
      color: white;
    }

    ul#feedbackList {
      list-style-type: none;
      padding-left: 0;
    }

    ul#feedbackList li {
      padding: 8px 10px;
      background: #eef6ff;
      border-left: 5px solid #2980b9;
      margin-bottom: 10px;
      border-radius: 6px;
    }
    body.dark {
  background: #1e1e1e;
  color: #f0f0f0;
}

body.dark .container {
  background: #2c2c2c;
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
}

body.dark .section {
  background: #3a3a3a;
  border-left-color: #00b894;
}

body.dark th {
  background: #00b894;
  color: #fff;
}

body.dark ul#feedbackList li {
  background: #2e2e2e;
  border-left-color: #00cec9;
}

  </style>
</head>
<body>
  <div class="container">
    <div style="text-align: right;">
  <label>
    <input type="checkbox" id="themeToggle" />
    🌗 Toggle Dark Mode
  </label>
</div>

    <h1>AI Career & Resume Analyzer</h1>
    <form id="resumeForm">
      <input type="file" id="resume" name="resume" accept=".pdf,.docx" required />
      <br>
      <button type="submit">🔍 Analyze My Resume</button>
    </form>

    <div id="result">
      <div class="section">
        <h2>📄 Resume Info</h2>
        <p><strong>Name:</strong> <span id="name"></span></p>
        <p><strong>Email:</strong> <span id="email"></span></p>
        <p><strong>Phone:</strong> <span id="phone"></span></p>
        <p><strong>Education:</strong> <span id="education"></span></p>
        <p><strong>Skills:</strong> <span id="skills"></span></p>
      </div>

      <div class="section">
        <h2>🎯 Job Role Match Scores</h2>
        <table id="roleScores">
          <thead>
            <tr>
              <th>Job Role</th>
              <th>Match Score (%)</th>
            </tr>
          </thead>
          <tbody></tbody>
        </table>
      </div>

      <div class="section">
        <h2>🧠 Smart Resume Feedback</h2>
        <ul id="feedbackList"></ul>
      </div>
    </div>
  </div>

  <script>
    document.getElementById('resumeForm').addEventListener('submit', async function (e) {
      e.preventDefault();
      const formData = new FormData();
      const fileInput = document.getElementById('resume');
      formData.append('resume', fileInput.files[0]);

      const response = await fetch('/upload', { method: 'POST', body: formData });
      const data = await response.json();

      document.getElementById('result').style.display = 'block';
      document.getElementById('name').innerText = data.name || "N/A";
      document.getElementById('email').innerText = data.email || "N/A";
      document.getElementById('phone').innerText = data.phone || "N/A";
      document.getElementById('education').innerText = data.education?.join(', ') || "N/A";
      document.getElementById('skills').innerText = data.skills?.join(', ') || "N/A";

      const tbody = document.querySelector('#roleScores tbody');
      tbody.innerHTML = "";
      for (let role in data.matched_roles) {
        const row = `<tr><td>${role}</td><td>${data.matched_roles[role]}%</td></tr>`;
        tbody.innerHTML += row;
      }

      const feedbackList = document.getElementById('feedbackList');
      feedbackList.innerHTML = "";
      for (let role in data.feedback) {
        const li = document.createElement('li');
        li.innerHTML = `<strong>${role}:</strong> ${data.feedback[role]}`;
        feedbackList.appendChild(li);
      }
      document.getElementById('themeToggle').addEventListener('change', function () {
  document.body.classList.toggle('dark');
});

    });
  </script>
</body>
</html>

