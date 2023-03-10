// FETCHING DATA FROM BACKEND
// api url
const api_url = "/participants/api/profiles/";

// PARTICIPANTS
const sectionCenter = document.querySelector(".participants-content");

// load participants
window.addEventListener("DOMContentLoaded", function () {
  async function getapi(url) {
    const response = await fetch(url);
    var data = await response.json();
    displayParticipants(data);
  }
  getapi(api_url);
});

// filter items
function displayParticipants(courseItems) {
  let displayParticipants = courseItems.map(function (participant) {
    return `    
      <div class="participants-card">
       <div class="participants-data">
         <div class="participants-data-title"><i class="fas fa-user" style="font-size: 1.2rem; padding-right: 5px;"></i>Name</div>
         <div class="participants-data-data">${participant.username}</div>
       </div>
       <div class="participants-data">
         <div class="participants-data-title"><i class="fas fa-clinic-medical" style="font-size: 1.2rem; padding-right: 5px;"></i>Hospital</div>
         <div class="participants-data-data">${participant.hospital}</div>
       </div>
       <div class="participants-data">
         <div class="participants-data-title"><i class="fas fa-user-tie" style="font-size: 1.2rem; padding-right: 5px;"></i>Profession</div>
         <div class="participants-data-data">${participant.profession}</div>
       </div>
       <div class="participants-data">
         <div class="participants-data-title"><i class="fas fa-sort-numeric-up" style="font-size: 1.2rem; padding-right: 5px;"></i>PIN</div>
         <div class="participants-data-data">${participant.pin}</div>
       </div>
       <div class="participants-data">
         <div class="participants-data-title"><i class="fas fa-envelope" style="font-size: 1.2rem; padding-right: 5px;"></i>Email</div>
         <div class="participants-data-data">${participant.email}</div>
       </div>
       <div class="participants-data">
         <div class="participants-data-title"><i class="fas fa-venus-mars" style="font-size: 1.2rem; padding-right: 5px;"></i>Gender</div>
         <div class="participants-data-data">${participant.gender}</div>
       </div>
      </div>`;
  });
  displayMenu = displayParticipants.join("");
  sectionCenter.innerHTML = displayMenu;
}
