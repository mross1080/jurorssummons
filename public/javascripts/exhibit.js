var visitorId = ""

const ws = new WebSocket('ws://localhost:8080');

ws.onopen = function (event) {
    ws.send("Here's some text that the server is urgently awaiting!");
  };
function initFingerprintJS() {
    FingerprintJS.load().then(fp => {
      fp.get().then(result => {
        // This is the visitor identifier:
        visitorId = result.visitorId;
        console.log(visitorId);
        retrieveUserData()
      });
    });
  }

function retrieveUserData() {
  fetch(`/retrieveUser?fingerprintId=${visitorId}`)
.then(
  function(response) {
    if (response.status !== 200) {
      console.log('Looks like there was a problem. Status Code: ' +
        response.status);
      return;
    }

    // Examine the text in the response
    response.json().then(function(data) {
        console.log("Look at this data!")
        let userData = (JSON.parse(data.name))
      console.log(JSON.parse(data.name));
      document.getElementById("name").innerText = `Hello ${userData.userName}`

    });
  }
)
.catch(function(err) {
  console.log('Fetch Error :-S', err);
});

}


  function submitAnswer(stationName) {

    // var answer = document.getElementById("answer").value
    var answer = document.forms["answerForm"].elements["answerOption"].value
    console.log(`sending answer ${answer} to /${stationName}?fingerprintId=${visitorId}&answer=${answer}`)
    fetch(`/${stationName}answer?fingerprintId=${visitorId}&answer=${answer}`)
    .then(
      function(response) {
        if (response.status !== 200) {
          console.log('Looks like there was a problem. Status Code: ' +
            response.status);
          return;
        }
    
        // Examine the text in the response
        response.json().then(function(data) {
            console.log("Look at this data!")
          console.log(data);
          $("#ex1").modal({
            fadeDuration: 300
          });
    
        });
      }
    )
    .catch(function(err) {
      console.log('Fetch Error :-S', err);
    });

    

  }


function getNewVal() {

}
