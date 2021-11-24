// const modalBtn = document.querySelector(".modal-btn");
courses = [
  {
    id: 1,
    img: "https://source.unsplash.com/286x200/weekly?programming",
    course: "A",
  },
  {
    id: 2,
    img: "https://source.unsplash.com/286x200/weekly?technology",
    course: "B",
  },
  {
    id: 3,
    img: "https://source.unsplash.com/286x200/weekly?nature",
    course: "C",
  },
  {
    id: 4,
    img: "https://source.unsplash.com/286x200/weekly?water",
    course: "D",
  },
  {
    id: 5,
    img: "https://source.unsplash.com/286x200/weekly?programming",
    course: "E",
  },
  {
    id: 6,
    img: "https://source.unsplash.com/286x200/weekly?football",
    course: "F",
  },
  {
    id: 7,
    img: "https://source.unsplash.com/286x200/weekly?world",
    course: "F",
  },
  {
    id: 8,
    img: "https://source.unsplash.com/286x200/weekly?chart",
    course: "F",
  },
];

// COURSES CARD
const sectionCenter = document.querySelector(".section-center");

// load items
window.addEventListener("DOMContentLoaded", function () {
  displayCourses(courses);
});

// filter items
function displayCourses(courseItems) {
  let displayCourse = courseItems.map(function (course) {
    return `    
      <div class="card m-2 my-3" style="max-width: 18rem">
        <img src="${course.img}" class="card-img-top" alt="${course.course}" />
        <div class="card-body p-3 m-0 text-center">
          <a href="/medical/export/excel/">
            <button type="button" class="btn btn-primary my-1 text-center">
              <i class="fas fa-download" style="padding: 5px"></i></button
          ></a>
          <button type="button" class="modal-btn btn btn-primary my-1 text-center">
            <i class="fas fa-upload" style="padding: 6px"></i>
          </button>
        </div>
      </div>`;
  });
  displayMenu = displayCourse.join("");
  sectionCenter.innerHTML = displayMenu;
}
// COURSES END

// MODAL UPLOAD

const modal = document.querySelector(".modal-overlay");
const closeBtn = document.querySelector(".close-btn");

// document.addEventListener("DOMContentLoaded", function () {
//   const modalBtn = element.getElementsByClassName("modal-btn");
//   var arr = Array.prototype.slice.call(modalBtn);
//   console.log(arr);
//   console.log(modalBtn);
// });

// closeBtn.addEventListener("click", function () {
//   modal.classList.remove("open-modal");
// });
// MODAL UPLOAD END

// console.log(Array.from(modalBtn));
// Array.from(modalBtn).forEach(function (btn) {
//   btn.addEventListener("click", function () {
//     console.log("I AM CLICKED>>>>>>>>");
//   });
// });
// Mbtn.map(function (btn) {
//   btn.addEventListener("click", function () {
//     console.log("i am clicked");
//     modal.classList.add("open-modal");
//   });
// });

// modalBtn.addEventListener("click", function () {
//   modal.classList.add("open-modal");
// });
