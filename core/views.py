# core/views.py
from django.shortcuts import render
from django.http import Http404
# Mock database of your actual projects
PROJECTS_DATA = {
    'lapo-marpaung': {
        'title': 'Lapo Marpaung',
        'subtitle': 'WEB DEVELOPMENT / E-COMMERCE MOCK UP',
        'description': 'Developed a web-based e-commerce platform and food marketplace for a fictional restaurant, featuring comprehensive digital menus and seamless transaction processing.',
        'role': 'Project Manager (Group Project)',
        'year': '2025',
        'type': 'Web Engineering',
        'status': 'INACTIVE',
        'stack': ['HTML/CSS', 'Python', 'Django', 'SQL'],
        'live_demo': 'https://kelompok-46-lapo-marpaung.pkpl.cs.ui.ac.id/',
        'image': 'core\images\lapo_marpaung.jpeg',
    },
    'angkringan-pedia': {
        'title': 'Angkringan Pedia',
        'subtitle': 'WEB DEVELOPMENT / E-COMMERCE MOCK UP',
        'description': 'Designed and built a web-based e-commerce application aimed at discovering local street food (angkringan) spots, including interactive food spot cataloging, category filtering, and a community review system.',
        'role': 'Backend & UI Designer (Group Project)',
        'year': '2024',
        'type': 'Web Engineering',
        'status': 'INACTIVE',
        'stack': ['HTML/CSS', 'Python', 'Django', 'Flutter'],
        'live_demo': 'https://kelompok-46-lapo-marpaung.pkpl.cs.ui.ac.id/',
        'image': 'core/images/angkringan_pedia.jpeg',
    },
    'pet-clinic': {
        'title': 'Pet Clinic',
        'subtitle': 'INFORMATION SYSTEMS WEBSITE',
        'description': 'Developed a web-based clinical information system featuring role-based access control to optimize workflows for doctors, nurses, and clients, with tracking and monitoring modules of pet health status and medical conditions.',
        'role': 'Database & Developer (Group Project)',
        'year': '2025',
        'type': 'Enterprise System',
        'status': 'INACTIVE',
        'stack': ['HTML/CSS', 'Python', 'Django','Java', 'Spring Boot', 'PostgreSQL', 'RBAC Architecture'],
        'live_demo': 'https://early-unicorn-tk3-basdat-e-0e3f6d45.koyeb.app/',
        'image': 'core/images/pet_clinic.jpeg',
    },
    'paxellms': {
        'title': 'PaxelLMS',
        'subtitle': 'KNOWLEDGE MANAGEMENT SYSTEM',
        'description': 'Created a Figma prototype for an organizational Knowledge Management System, integrated advanced features including an AI chatbot, expertise locator, SOP repository, and collaborative discussion forums.',
        'role': 'KM Analyst (Group Project)',
        'year': '2026',
        'type': 'Application Design',
        'status': 'ACTIVE',
        'stack': ['Figma', 'Wireframing', 'AI Frameworks', 'Knowledge Management'],
        'live_demo': 'http://ristek.link/PaxelLMS',
        'image': 'core\images\paxellms.jpeg',
    },
    'kasirku': {
        'title': 'Kasirku',
        'subtitle': 'CANTEEN INFORMATION SYSTEMS',
        'description': 'Designed an ICT4D Figma prototype tailored for canteens across Universitas Indonesia focused on empowering local vendors by streamlining income tracking and fostering digital literacy.',
        'role': 'Product Designer (Group Project)',
        'year': '2026',
        'type': 'ICT4D / UX Design',
        'status': 'ACTIVE',
        'stack': ['Figma', 'UX Research', 'Application Design'],
        'live_demo': 'https://www.figma.com/proto/WQTlnVtc0vsBgmCgy5Jl8s/Mock-up-KasirKu?node-id=19-139&p=f&t=THCkglVUQxi6Eg8s-1&scaling=scale-down&content-scaling=fixed&page-id=0%3A1',
        'image': 'core\images\kasirku.jpeg',
    },
    'nihao': {
        'title': 'NiHao',
        'subtitle': 'MOBILE LEARNING APPLICATION',
        'description': 'Developed "NiHao," a mobile application prototype using Figma aimed at interactive Chinese language learning. Incorporated engaging features such as learning paths, quizzes, forums, and media integration.',
        'role': 'Mobile UI Designer (Group Project)',
        'year': '2025',
        'type': 'EdTech Mobile',
        'status': 'ACTIVE',
        'stack': ['Figma', 'Mobile UI', 'Interaction Design'],
        'live_demo': 'https://www.figma.com/proto/UtG1DYs2MSbH3DUXF4GRjq/Ni-Hao---Template-4?page-id=107%3A4&node-id=1157-11640&viewport=625%2C-278%2C0.18&t=utA2D8n0tSTPqCvm-1&scaling=scale-down&content-scaling=fixed&starting-point-node-id=1157%3A11640',
        'image': 'core/images/nihao.jpeg',
    },
}

def index(request):
    # Pass the projects dictionary to the homepage template
    return render(request, 'core/index.html', {'projects': PROJECTS_DATA})

def project_detail(request, project_slug):
    # Fetch project details using the URL slug string
    project = PROJECTS_DATA.get(project_slug)
    if not project:
        raise Http404("Project not found")
    return render(request, 'core/project_detail.html', {'project': project})

def about(request):
    return render(request, 'core/about.html')