

SmartStock API 📦
A professional-grade Inventory Management & Procurement Automation System designed to streamline cafe operations and minimize manual stock tracking overhead.

🚀 Business Impact
Manual inventory monitoring is error-prone and inefficient. SmartStock API automates the procurement lifecycle by:

Detecting low-stock thresholds in real-time.

Automating supplier communication via email triggers.

Reducing database load through optimized ORM queries.

🛠 Technical Stack
Framework: Django, Django REST Framework (DRF)

Database: PostgreSQL (with SQLite for local dev)

Authentication: JWT (JSON Web Tokens)

Utilities: SMTP (Automated Emailing)

Manual_Testing:Insomnia Test API

Infrastructure: Python 3.14.4, Git

⚙️ Core Technical Highlights
Database Optimization: Utilized Django F() at the database level, drastically reducing application-side memory overhead.

Automated Procurement: Implemented event-driven business logic that monitors stock levels vs. reorder points, triggering automated supplier restock notifications via EMAIL.

API Architecture: Followed RESTful principles to build scalable endpoints with granular RBAC (Role-Based Access Control) using JWT authentication.

Performance & Stability: Configured pagination, ordering filters, and robust exception handling for consistent API response quality (HTTP status codes 200, 400, 404, 500).

Serializer-Level Gatekeeping: Implemented custom validate() methods to act as a barrier between the user and the database.

Custom Constraint Enforcement: The system enforces specific business rules (e.g., rejecting bookings that exceed 10kg) before the data is committed. This prevents invalid data from ever reaching the database, ensuring consistent inventory states.

Resilient Input Handling: By using defensive coding practices, the API rejects bad data with clear, informative error messages (HTTP 400 Bad Request), rather than crashing.
Error Prevention: By validating inputs at the service entry point, the system prevents runtime exceptions and maintains a reliable state, ensuring the API is resilient against bad data inputs.

Screen Shots :

<img width="1918" height="827" alt="image" src="https://github.com/user-attachments/assets/344e52bc-9d80-46ae-91aa-9b0959d949e6" />
<img width="1918" height="605" alt="image" src="https://github.com/user-attachments/assets/a0791f22-78b8-4c54-9d92-17eb87668105" />
validation error
<img width="1836" height="363" alt="image" src="https://github.com/user-attachments/assets/4354049d-0ec8-4a41-9040-4654fe2a3ec2" />
This picture depicts that  auto email sent
<img width="1578" height="847" alt="image" src="https://github.com/user-attachments/assets/0bdf7703-07c1-4716-a61e-87e33ee893f8" />
<img width="835" height="547" alt="image" src="https://github.com/user-attachments/assets/91bbcf2c-a9f2-4cd5-b5f8-cc6bb6596212" />


📥 Getting Started
Clone the repository:
Bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install Dependencies:

Bash
pip install -r requirements.txt
Run Migrations & Start Server:

Bash
python manage.py migrate
python manage.py runserver
💡 Future Scope
Integration with a React/Next.js frontend.

Dashboard reporting via Data Visualization libraries (Chart.js/D3).

Docker containerization for production deployment.
