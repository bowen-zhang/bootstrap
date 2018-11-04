// Copyright 2018 Bowen Zhang
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Initialize Firebase
var config = {
  apiKey: "[apiKey]",
  databaseURL: "[databaseURL]",
  projectId: "[projectId]",
};
firebase.initializeApp(config);
var db = firebase.firestore();
db.settings({
	timestampsInSnapshots: true
});

db.collection('messages').orderBy('timestamp').onSnapshot(querySnapshot => {
	document.getElementById('messageList').innerHTML = '';
	querySnapshot.forEach(doc => {
		newMessage(doc.data());
	})
});

function send() {
	var text = document.getElementById('text').value;
	db.collection('messages').add({
		timestamp: new Date(),
		text: text
	})
	.then(docRef => {
		console.log('sent');
	});
}

function newMessage(message) {
	newElement = document.createElement('div');
	newElement.innerText = `${message.timestamp.toDate().toLocaleString()}: ${message.text}`;
	document.getElementById('messageList').appendChild(newElement);
}

document.getElementById('send').addEventListener('click', send);