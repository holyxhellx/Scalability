

window.onload=function(){
    var userSettings = document.getElementById('user');
    var settingsSettings = document.getElementById('settings');
    var sidebarUser = document.getElementById('sidebarUser');
    var backgroundOverlay = document.getElementById('background-overlay');
    var addNewButton = document.getElementById('add-new-button');

    userSettings.addEventListener("click", function(){
        if(sidebarUser.classList.contains("activeSidebar")){
            sidebarUser.classList.remove("activeSidebar");
            backgroundOverlay.style.display = 'none';

        }else{
            sidebarUser.classList.add("activeSidebar");
            backgroundOverlay.style.display = 'block';
        }
    });

    settingsSettings.addEventListener("click", function(){
        if(sidebarUser.classList.contains("activeSidebar")){
            sidebarUser.classList.remove("activeSidebar");
            backgroundOverlay.style.display = 'none';

        }else{
            sidebarUser.classList.add("activeSidebar");
            backgroundOverlay.style.display = 'block';
        }
    });

    backgroundOverlay.addEventListener("click", function(){
            if(sidebarUser.classList.contains("activeSidebar")){
                sidebarUser.classList.remove("activeSidebar");
                backgroundOverlay.style.display = 'none';

            }
            document.getElementById('create-new-jodel').style.display = 'none';
            backgroundOverlay.style.display = 'none';



    });

    addNewButton.addEventListener("click", function(){
        document.getElementById('create-new-jodel').style.display = 'block';
        backgroundOverlay.style.display = 'block';


    });

}
