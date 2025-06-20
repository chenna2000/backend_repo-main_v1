from django.urls import path # type: ignore
from . import views
from .views import  CollegeListCreateView,  CompanyListCreateView, CompanyDetailView

urlpatterns = [
    path('home', views.home, name='home'),
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),

    ## Company Dashboard
    path('company-status-counts/<int:company_in_charge_id>/', views.company_status_counts, name='company_status'),
    path('companies/<int:company_in_charge_id>/', CompanyListCreateView.as_view(), name='company_list_create'),
    path('create-company-jobs/<int:company_in_charge_id>/', views.create_company_jobs, name='create_company_jobs'),
    path('jobs-by-company/<int:company_in_charge_id>/', views.jobs_by_company, name='jobs_by_company'),
    path('fetch-applicants/<int:company_in_charge_id>/', views.fetch_company_applicants_count, name='fetch_applicants'),
    path('update-company-application-status/<int:company_in_charge_id>/<int:application_id>/', views.update_company_application_status, name='update_company_application_status'),
    path('job-application-summary/<int:company_in_charge_id>/', views.get_job_application_summary, name='job_application_summary'),
    path('get-application-details/<int:company_in_charge_id>/', views.get_application_details, name='get_application_details'),
    path('update-company-job/<int:company_in_charge_id>/<int:job_id>/', views.update_company_job, name= "update-company-job"),
    path('change-company-job-status/<int:company_in_charge_id>/<int:job_id>/', views.change_company_job_status, name= "change_company_job_status"),
    path('company-job-applications/<int:company_in_charge_id>/<int:job_id>/', views.fetch_company_job_applications, name='fetch_job_applications'),
    # Not Used
    path('save-questions-answers-company/<int:company_in_charge_id>/', views.save_screening_questions_and_answers_for_company, name='save_questions_answers_company'),
    path('submit-screening-answers-company/<int:job_id>/<int:company_in_charge_id>/', views.submit_application_with_screening_for_company, name='submit-screening-answers_company'),
    path('schedule-interview/<int:company_in_charge_id>/', views.schedule_interview_from_company, name='schedule-interview'),
    path('upcoming/<int:company_in_charge_id>/', views.get_upcoming_interviews_from_company, name='upcoming_interviews'),
    path('past/<int:company_in_charge_id>/', views.get_past_interviews_from_company, name='past_interviews'),
    path('company-membership/<int:company_in_charge_id>/', views.membership_form_view, name='membership_form'),
    path('company-advertisement/<int:company_in_charge_id>/', views.advertisement_form_view, name='advertisement_form'),


    ## College Dashboard
    path('college_status_counts/<int:university_in_charge_id>/', views.college_status_counts, name='submit-enquiry'),#
    path('colleges/<int:university_in_charge_id>/', CollegeListCreateView.as_view(), name='college_list_create'),#
    path('college-create-job/<int:university_incharge_id>/', views.create_job_for_college, name='college-create-job'),#
    path('jobs-by-college/<int:university_in_charge_id>/', views.jobs_by_college, name='jobs-by-college'),#
    path('update-college-job/<int:university_incharge_id>/<int:job_id>/', views.update_college_job, name= "update-college-job"),#
    path('change-college-job-status/<int:university_incharge_id>/<int:job_id>/', views.change_college_job_status, name= "change_college_job_status"),#
    path('fetch-student-enquiries/<int:university_in_charge_id>/', views.get_student_enquiries_for_college, name='fetch-student-enquiries'),#
    path('update-college-application-status/<int:university_in_charge_id>/<int:application_id>/', views.update_college_application_status, name='update_college_application_status'),
    path('fetch-college-jobs/<int:college_id>/<int:university_in_charge_id>/', views.college_jobs_api, name='fetch-college-jobs'),#
    path('fetch-college-jobs/<int:college_id>/<int:university_in_charge_id>/<int:job_id>/', views.job_detail_api, name='fetch-college-jobsdetails'),#
    path('fetch-college-applicants/<int:university_in_charge_id>/', views.fetch_college_applicants_count, name='fetch_applicants_counts'),#
    # Not used
    path('college-advertisement/<int:university_in_charge_id>/', views.advertisement_form_view1, name='advertisement_form'),
    path('college-membership/<int:university_in_charge_id>/', views.membership_form_view1, name='membership_form'),
    path('save-questions-answers-college/<int:university_incharge_id>/', views.save_screening_questions_and_answers_for_college, name='save_questions_answers_college'),
    path('submit-screening-answers-college/<int:job_id>/<int:university_incharge_id>/', views.submit_application_with_screening_for_college, name='submit-screening-answers_college'),
    path('register-visitor/<int:university_in_charge_id>/', views.register_visitor, name='register-visitor'),
    path('login-visitor/<int:university_in_charge_id>/', views.login_visitor, name='login-visitor'),
    # path('student-enquiries-for-college/<int:college_id>/<int:university_in_charge_id>/', views.student_enquiries_for_college, name='student-enquiries-for-college'),


    ## Candidate Dashboard
    path('jobseeker-application-status-counts/<int:jobseeker_id>/', views.jobseeker_application_status_counts, name='jobseeker_application_status_counts'),#
    path('fetch-jobseeker-applied-jobs/<int:jobseeker_id>/', views.filterjobseeker__applied_jobs, name='filter_applied_jobs'),#
    path('create-jobseeker-resume/<int:jobseeker_id>/', views.create_jobseeker_resume, name='create_jobseeker_resume'),#
    path('jobseeker_resume/<int:jobseeker_id>/', views.get_jobseeker_resume_detail_by_id, name='get_jobseeker_resume_detail_by_id'),#
    path('fetch-jobs/<int:job_seeker_id>/', views.fetch_jobs_by_job_seeker_skills, name='fetch-skills'),#
    path('jobseeker-apply-job/<int:job_id>/<int:jobseeker_id>/', views.jobseeker_apply_for_job, name='jobseeker-apply-job'),#
    path('save-job/', views.save_job, name='save_job'),#
    path('unsave-job/', views.unsave_job, name='unsave_job'),#
    path('fetch-saved-jobs/<int:jobseeker_id>/', views.fetch_saved_jobs, name='fetch_saved_jobs'),#
    
    # Not used
    path('interviews/upcoming/<int:job_seeker_id>/', views.get_upcoming_interviews_by_job_title, name='get_upcoming_interviews_by_job_role'),
    path('interviews/past/<int:job_seeker_id>/', views.get_past_interviews_by_job_title, name='get_past_interviews_by_job_role'),


    ## Student Dashboard
    path('user-application-status-counts/<int:user_id>/', views.user_application_status_counts, name='user_application_status_counts'),#
    path('fetch-user-applied-jobs/<int:user_id>/', views.filter_user_applied_jobs, name='filter_applied_jobs'),#
    path('create_resume/<int:user_id>/', views.create_user_resume, name='create_resume'),#
    path('resume/<int:user_id>/', views.get_user_resume_detail_by_id, name='get_resume_detail_by_id'), #
    path('fetch-user-skills-jobs/<int:user_id>/', views.fetch_jobs_by_new_user_skills, name='fetch-skills'),#
    path('save-job-new-user/', views.save_job_new_user, name='save_job_new_user'),#
    path('unsave-job-new-user/', views.unsave_job_new_user, name='unsave_job_new_user'),#
    path('fetch-saved-jobs-new-user/<int:new_user_id>/', views.fetch_saved_jobs_new_user, name='fetch_saved_jobs_new_user'),#
    path('user-apply-job/<int:job_id>/<int:user_id>/', views.user_apply_for_job, name='user-apply-job'), #
    path('new-user-enquiry/<int:id>/', views.submit_enquiry, name= "submit_enquiry"),#

    # Not used
    path('get-student-enquiries/<int:user_id>/', views.get_user_enquiries, name='user-enquiries'),
    path('submit-college-enquiry/<int:university_in_charge_id>/', views.submit_college_enquiry, name='submit-college-enquiry'),



    ## extra functionalities (Not Used)
    path('jobs/', views.job_list, name='job_list'),
    path('jobs-showcase/', views.job_list_showcase, name='job_list'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('applications/<int:job_id>/', views.job_applications, name='job_applications'),
    path('job-status/<int:job_id>/', views.job_status, name='job_status'),
    path('fetch-companies/', views.fetch_all_companies, name='fetch-companies'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),
    path('find_status/', views.find_status, name="find_status"),
    path('candidate_profile/', views.candidate_profile, name ="candidate_profile"),
    path('category_with_count/', views.count_jobs_by_category, name='category_with_count'),
    path('fetch_jobs/', views.fetch_jobs_by_exp_skills, name='fetch_jobs'),
    path('fetch_jobs_category/', views.fetch_jobs_by_category_location_skills, name='fetch_jobs_category'),
    path('get_job_titles/', views.fetch_job_titles, name='get_job_titles'),
    path('get_job_types/', views.fetch_job_types, name='get_job_types'),
    path('get_job_experince/', views.fetch_job_experience, name='get_job_experince'),
    path('get_job_category/', views.fetch_job_category, name='get_job_category'),
    path('get_job_workplaceTypes/', views.fetch_job_workplaceTypes, name='get_job_workplaceTypes'),
    path('get_job_location/', views.fetch_job_location, name='get_job_location'),
    path('fetch_sector_types/', views.fetch_sector_types, name='fetch_sector_types'),
    path('fetch_contry_types/', views.fetch_country_types, name='fetch_contry_types'),
    path('fetch_status/', views.fetch_status_choices, name='fetch_status'),
    path('sort-saved-jobs/', views.sort_saved_jobs, name='sort-saved-jobs'),
    path('create-job-alerts/', views.create_job_alert, name='create-job-alert'),
    path('save-student/<int:user_id>/', views.save_student, name='save-student'),
    path('fetch-clg-jobs/', views.fetch_colleges_jobs, name='fetch-clg-jobs'),
    path('fetch-colleges/', views.fetch_colleges, name='fetch-colleges'),
    path('apply/<int:job_id>/<int:company_in_charge_id>/', views.apply_job, name='apply_job'),
    path('company_status/<str:status_choice>/<int:company_in_charge_id>/', views.company_status, name= "company_status"),
    path('apply-college-job/<int:job_id>/<int:university_in_charge_id>/', views.apply_college_job, name='apply-college-job'),
    path('college_status/<str:status_choice>/<int:university_in_charge_id>/', views.college_status, name= "college_status"),
]
