**System Context & Tech Stack:**
You are an expert Full-Stack Enterprise Developer. I need you to scaffold a Minimum Viable Product (MVP) for an operational data portal. 
* **Frontend:** React (TypeScript, Vite, Tailwind CSS, React Router, Recharts for dashboards).
* **Backend:** .NET 8 Web API (C#).
* **Authentication:** Microsoft Entra ID (MSAL for React, `Microsoft.Identity.Web` for .NET).
* **Database Access:** Dapper (for high-performance querying) connecting to SQL Server / Snowflake.
* **PDF Generation:** QuestPDF (in the .NET backend).

**Architecture Rules:**
1. Use the Repository Pattern in the .NET backend to abstract database calls. The app will connect to the database using a single backend Service Account connection string securely stored in `appsettings.json` (or environment variables).
2. Implement Row-Level Security logic at the API controller level based on Entra ID user roles.
3. Ensure strict separation of concerns. The frontend only handles UI and routing; the backend handles all business logic, data processing, and PDF generation.

**Required MVP Features to Scaffold:**
1.  **Authentication Layer:** Scaffold the MSAL wrapper in React to require Office 365 login before viewing any page. Scaffold the `[Authorize]` middleware in the .NET API.
2.  **Landing Page / Nav Bar:** A clean, responsive home page with a sidebar navigation containing links to Profile, Dashboards, Reports, and Insights.
3.  **User Profile:** A simple page displaying the logged-in user's Entra ID claims (Name, Email, Role).
4.  **Dashboards View:** A React component utilizing `Recharts` to display mock operational data (e.g., incident response times, inventory levels). Create a corresponding .NET API endpoint `GET /api/dashboards/summary` that returns mock JSON data.
5.  **PDF Reports Module:** * *Frontend:* A form with date pickers and category dropdowns to filter data. A "Generate Report" button that calls the backend.
    * *Backend:* An endpoint `POST /api/reports/generate` that accepts the filter parameters, mocks fetching data, and uses QuestPDF to generate a byte array of a PDF document, returning it to the frontend for download.
6.  **Insights (Custom Builder):** A placeholder view where users can select X and Y axes from dropdowns to dynamically render a chart based on a generic API endpoint `GET /api/insights/query`.

**Execution Steps for the Agent:**
1. Generate the folder structure for both the frontend (`/client`) and backend (`/api`).
2. Provide the `Program.cs` configuration for Entra ID and CORS.
3. Provide the foundational React components for the routing and navigation.
4. Implement the mock API controllers for the Dashboards and PDF generation.