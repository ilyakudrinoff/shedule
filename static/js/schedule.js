function accordion() {
    document.querySelectorAll(".accordion").forEach(el=>{
    el.addEventListener("click",e=>{
    	e.currentTarget.nextElementSibling.classList.toggle("active");
    });
});
}
