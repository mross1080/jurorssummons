var visitorId = ""
var lang = "en"

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

      if (userData.lang === "en") {
        $(".esContent").hide()
        $("#langEn").css("border-bottom","3px solid white")

      } else {
        lang = "es"
        $(".enContent").hide()
        $("#langEs").css("border-bottom","3px solid white")

      }

      $("#ex2").modal({
        fadeDuration: 500
      });
      document.getElementById("name").innerText = ` ${userData.userName}`


   
      setTimeout(function() { $(".blocker").click()}, 3000)





    });
  }
)
.catch(function(err) {
  console.log('Fetch Error :-S', err);
});

}


  function submitAnswer(stationName) {
    var answer = ""

    if (stationName == "print") {
      answer = "ready"
    } else {
      answer = document.forms[`answerForm${lang}`].elements["answerOption"].value
    }


    // var answer = document.getElementById("answer").value
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

    

          document.getElementById("nextStationLink").click()
    
        //   setTimeout(function() {
        //     conso  
        //     $(".blocker").click()}, 3000)

        });
      }
    )
    .catch(function(err) {
      console.log('Fetch Error :-S', err);
    });

    

  }


function getNewVal() {

}
