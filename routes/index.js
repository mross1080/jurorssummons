var express = require('express');
var router = express.Router();
const redis = require('redis');
const WebSocket = require('ws');

const client = redis.createClient({
  host: 'redis-14390.c256.us-east-1-2.ec2.cloud.redislabs.com',
  port: '14390',
  password: 'EEDPLADvHhC12ziP5B2m2skqO7ZRv24i'
});


/* GET home page. */
router.get('/', function (req, res, next) {

   res.render('index', { 
    title: 'Jurors Summons',
     station: 'Welcome Station',
    submit:"Submit",
    namePlaceholder:"Your Name",
    modalMessage:"Thank you for your answer. You may now proceed to the next station "
   });
});


router.get('/es', function (req, res, next) {

  res.render('index', { 
    title: 'Jurors Summons',
     station: 'Welcome Station',
    submit:"Someter",
    namePlaceholder:"Su Nombre",
    modalMessage:"Gracias por su respuesta. Ahora puede pasar a la siguiente estación"
   });
});


/* GET home page. */
router.get('/station', function (req, res, next) {

  res.render('station', { title: 'Jurors Summons', station: 'Welcome Station' });
});

router.get('/stationone/', function (req, res, next) {
  console.log(req)

  res.render('stationone', { title: 'Jurors Summons', station: 'Welcome Station' });
});

router.get('/stationtwo', function (req, res, next) {

  res.render('stationtwo', { title: 'Jurors Summons', station: 'Welcome Station' });
});

router.get('/stationthree', function (req, res, next) {

  res.render('stationthree', { title: 'Final Station', station: 'Welcome Station' });
});

router.get('/zipcode', function (req, res, next) {

  res.render('zipcode', { title: 'Jurors Summons', station: 'Welcome Station' });
});

router.get('/print', function (req, res, next) {

  res.render('print', { title: 'Jurors Summons', station: 'Welcome Station' });
});


router.get('/sugarIntake', function (req, res, next) {

  res.render('sugarIntake', { title: 'Jurors Summons', station: 'Welcome Station' });
});


router.get('/archivePermission', function (req, res, next) {

  res.render('archivePermission', { title: 'Jurors Summons', station: 'Welcome Station' });
});



function setAnswerForStation(res, station, userId, answer) {

  try {


    client.get(userId, (err, reply) => {
      if (err) {
        console.log(err)
      }
      let userInfo = JSON.parse(reply)

      if (userInfo != null) {

        console.log("Got user info ", userInfo)

        userInfo[station] = answer
        client.set(userId, JSON.stringify(userInfo), (err, reply) => {
          if (err) {
            console.log(err)
            res.json({ title: "Error In Submitting Answer" });

          }
          console.log("r : " + reply);
          res.json({ title: "Update Successful" });
        })



      } else {
        console.log("Could not find user ")
      }

    });
  } catch (err) {
    console.log(err)
    res.json({ title: "Update Failure" });

  }


}





router.get('/stationoneanswer', function (req, res, next) {
  console.log("Got answer at station 1  ")
  console.log(req.query)

  setAnswerForStation(res, "a1", req.query.fingerprintId, req.query.answer)
});

router.get('/stationtwoanswer', function (req, res, next) {
  console.log("Got new answer for station two  ")
  console.log(req.query)

  setAnswerForStation(res, "a2", req.query.fingerprintId, req.query.answer)
});


router.get('/stationthreeanswer', function (req, res, next) {
  console.log("Sending data for station 3  ")
  console.log(req.query)
  let wss = req.app.get("wss")
  // console.log(wss)
  let userId = req.query.fingerprintId
  console.log("Attempting to create redis connection")


  setAnswerForStation(res, "a3", req.query.fingerprintId, req.query.answer)
});


router.get('/sugarIntakeanswer', function (req, res, next) {
  console.log("Sending data for station 3  ")
  console.log(req.query)


  setAnswerForStation(res, "sugarIntake", req.query.fingerprintId, req.query.answer)
});

router.get('/archivePermissionanswer', function (req, res, next) {
  console.log("Sending data for station 3  ")
  console.log(req.query)


  setAnswerForStation(res, "archivePermission", req.query.fingerprintId, req.query.answer)
});


router.get('/zipcodeanswer', function (req, res, next) {
  console.log("Got new user ")
  console.log(req.query)

  setAnswerForStation(res, "zipcode", req.query.fingerprintId, req.query.answer)
});

router.get('/printanswer', function (req, res, next) {
  console.log("Got command to print ")
  console.log(req.query)
  let userId = req.query.fingerprintId
  try {



    client.get(userId, (err, reply) => {
      if (err) {
        console.log(err)
      }

      console.log("got data structure for ", userId)

      let userInfo = JSON.parse(reply)

      console.log("sending data", userInfo)

      client.publish("broadcast",JSON.stringify(userInfo))

    });


  } catch (err) {
    console.log(err)
  }

});




let userInfo = {
  "userName": "",
  "userId": "",
  "a1": "",
  "a2": "",
  "a3": "",
  "zipcode": "",
  "sugarIntake":"",
  "archivePermission":""
}


router.get('/registerUser', function (req, res, next) {
  console.log("Got new user ")

  let userName = req.query.userName
  let fingerprintId = req.query.fingerprintId
  console.log("Username ", userName)
  console.log("Finger print id ", fingerprintId)

  userInfo["userName"] = userName
  userInfo["userId"] = fingerprintId

  client.set(fingerprintId, JSON.stringify(userInfo), (err, reply) => {
    if (err) {
      console.log(err)
    }
    console.log(reply);

    client.get(fingerprintId, (err, reply) => {
      if (err) {
        console.log(err)
      }
      console.log("r : " + reply);
      res.json({ title: JSON.parse(reply) });

    });
  });

  client.on('error', err => {
    console.log('Error ' + err);
  });



});

router.get('/retrieveUser', function (req, res, next) {
  console.log("Got new user ")

  let fingerprintId = req.query.fingerprintId
  console.log("Finger print id ", fingerprintId)



  client.get(fingerprintId, (err, reply) => {
    if (err) {
      console.log(err)
    }
    console.log("r : " + reply);
    res.json({ name: reply });

  });


  client.on('error', err => {
    console.log('Error ' + err);
  });



});


module.exports = router;
