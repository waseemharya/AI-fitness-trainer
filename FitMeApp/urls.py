from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name="index"),
    path("home", views.home, name="login"),
    path("contact", views.contact, name="contact"),
    path("seetask", views.seetask, name="seetask"),
    path("doneTask/<str:id>", views.doneTask, name="doneTask"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("gallery", views.gallery, name="gallery"),
    path("portal", views.portal, name="portal"),
    path("giveTask/<str:username>", views.giveTask, name="giveTask"),
    path(
        "portal/beginners-routines", views.beginners_routines, name="beginners_routines"
    ),
    path("beginner_day_1", views.beginner_day1, name="beginner_day1"),
    path("beginner_day_2", views.beginner_day2, name="beginner_day2"),
    path("beginner_day_3", views.beginner_day3, name="beginner_day3"),
    path("beginner_day_4", views.beginner_day4, name="beginner_day4"),
    path("beginner_day_5", views.beginner_day5, name="beginner_day5"),
    path("beginner_day_6", views.beginner_day6, name="beginner_day6"),
    path("beginner_day_7", views.beginner_day7, name="beginner_day7"),
    path("beginner_day_8", views.beginner_day8, name="beginner_day8"),
    path("beginner_day_9", views.beginner_day9, name="beginner_day9"),
    path("beginner_day_10", views.beginner_day10, name="beginner_day10"),
    path("beginner_day_11", views.beginner_day11, name="beginner_day11"),
    path("beginner_day_12", views.beginner_day12, name="beginner_day12"),
    path("beginner_day_13", views.beginner_day13, name="beginner_day13"),
    path("beginner_day_14", views.beginner_day14, name="beginner_day14"),
    path("beginner_day_15", views.beginner_day15, name="beginner_day15"),
    path("beginner_day_16", views.beginner_day16, name="beginner_day16"),
    path("beginner_day_17", views.beginner_day17, name="beginner_day17"),
    path("beginner_day_18", views.beginner_day18, name="beginner_day18"),
    path("beginner_day_19", views.beginner_day19, name="beginner_day19"),
    path("beginner_day_20", views.beginner_day20, name="beginner_day20"),
    path("beginner_day_21", views.beginner_day21, name="beginner_day21"),
    path("beginner_day_22", views.beginner_day22, name="beginner_day22"),
    path("beginner_day_23", views.beginner_day23, name="beginner_day23"),
    path("beginner_day_24", views.beginner_day24, name="beginner_day24"),
    path("beginner_day_25", views.beginner_day25, name="beginner_day25"),
    path("beginner_day_26", views.beginner_day26, name="beginner_day26"),
    path("beginner_day_27", views.beginner_day27, name="beginner_day27"),
    path("beginner_day_28", views.beginner_day28, name="beginner_day28"),
    path("portal/diet/beginner", views.diet_beginner, name="diet_beginner"),
    path("portal/diet/intermediate", views.diet_intermediate, name="diet_intermediate"),
    path("portal/diet/hardcore", views.diet_hardcore, name="diet_hardcore"),
    path("know_your_BMI_with_standard_unit", views.bmistandard, name="bmistandard"),
    path("know_your_BMI_with_metric_unit", views.bmimetric, name="bmimetric"),
    
    path("camera", views.camera, name="camera"),
    path("camera2", views.camera2, name="camera2"),
    path("camera3", views.camera3, name="camera3"),
    
    path("camera4", views.camera4, name="camera4"),
    path("camera5", views.camera4, name="camera5"),
    
    
    path("camera_vid", views.camera_vid, name="camera_vid"),
    path("camera2_vid", views.camera2_vid, name="camera2_vid"),
    path("camera3_vid", views.camera3_vid, name="camera3_vid"),
    path("camera4_vid", views.camera4_vid, name="camera4_vid"),
    path("camera5_vid", views.camera5_vid, name="camera5_vid"),
    
    path("fl_camera", views.fl_camera, name="fl_camera"),
    
    
    
    
    
    
    
    path("video", views.video, name="video"),
    
    path('video_feed/', views.video_feed, name='video_feed'),
    path('gym/', views.gym, name='gym'),
    path('signup/', views.signup, name='signup'),
    path('upload/', views.upload, name="upload"),    
    path('exc_plans/', views.exc_plans, name="exc_plans"),
    
    
    path('over/', views.over, name="over"),
    path('under/', views.under, name="under"),
    path('normal/', views.normal, name="normal"),
    path('refresh_system/', views.refresh_system, name="refresh_system"),
    
    

]

