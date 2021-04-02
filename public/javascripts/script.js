var visitorId = ""

function initFingerprintJS() {
    FingerprintJS.load().then(fp => {
      // The FingerprintJS agent is ready.
      // Get a visitor identifier when you'd like to.
      fp.get().then(result => {
        // This is the visitor identifier:
        visitorId = result.visitorId;
        console.log(visitorId);
        // document.getElementById("ip").innerText = `User Id ${visitorId}`
      });
    });
  }

function makeRequest(userName) {
  fetch(`/registerUser?fingerprintId=${visitorId}&userName=${userName}`)
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

function registerUser() {
    console.log("hi")
    let name  = document.forms["answerForm"].elements["answerOption"].value

    console.log(name)
    makeRequest(name)

}


function retrieveUser(userName) {
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
        console.log(data);
      });
    }
  )
  .catch(function(err) {
    console.log('Fetch Error :-S', err);
  });
  
  }

