fetch('https://55cf017q25.execute-api.us-east-1.amazonaws.com/Prod/count')
  .then((response) => response.json())
  .then((data) => {
    document.getElementById('count').innerText = data.message
  });
        