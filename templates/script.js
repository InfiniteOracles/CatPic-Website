window.onload = function () {
  // Get audio element
  var audio = document.getElementById("background-music");

  // Set the source of the audio file
  audio.src = "static/music.mp3"; // Replace 'static/music.mp3' with the actual path to your audio file

  // Play the audio
  audio.play();

  // Event listener to loop the audio when it ends
  audio.addEventListener("ended", function () {
    audio.currentTime = 0; // Reset audio to the beginning
    audio.play(); // Play again
  });
};
