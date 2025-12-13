importScripts('https://www.gstatic.com/firebasejs/9.22.1/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.22.1/firebase-messaging-compat.js');

firebase.initializeApp({
  apiKey: "AIzaSyDxr-d1ZKp3wt3i289o6FKmevr3s8Uw3WA",
  authDomain: "okuler.firebaseapp.com",
  projectId: "okuler",
  messagingSenderId: "853942864718",
  appId: "1:853942864718:web:337671e3596467ae7e6c1f"
});

const messaging = firebase.messaging();

messaging.onBackgroundMessage(payload => {
  self.registration.showNotification(
    "Neue Nachricht",
    {
      body: "Im SchulensteinChat gibt es eine neue Nachricht",
      icon: "icon-192.png"
    }
  );
});
