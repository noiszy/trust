function writeUserData(userId, name, email, imageUrl) {
  firebase.database().ref('users/' + userId).set({
    username: name,
    email: email,
    profile_picture : imageUrl
  });
}

function writeTestData(userId, name, email) {
  console.log("writing test data")
  firebase.database().ref('users/' + userId).set({
    username: name,
    email: email
  });
  console.log("written")
}