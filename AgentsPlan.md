### Agents - Plan

| Agent Name             | Core Role                       |
| ---------------------- | ------------------------------- |
| Claim Intake Agent     | Ingest + parse claim            |
| Validation Agent       | Check eligibility + consistency |
| Document Request Agent | Handle missing info loop        |
| Assessment Agent       | Analyze and estimate damages    |
| Decision Agent         | Approve or reject claim         |
| Query Answering Agent  | Serve claimants' questions      |
| Email Agent            | Write Email to user when necessary |

### Status Transitions

| **Status**     | **Triggered By**          | **Description**                                          |
| -------------- | ------------------------- | -------------------------------------------------------- |
| `RECEIVED`     | Claim Intake Agent        | Claim is parsed and entered into the system.             |
| `VALIDATED`    | Validation Agent          | Claim data and policy eligibility confirmed.             |
| `PENDING_INFO` | Document Request Agent    | Awaiting missing documents or clarification.             |
| `ASSESSED`     | Assessment Agent          | Claim damage or case reviewed and scored.                |
| `DECIDED`      | Decision Agent            | Final decision has been made.                            |
| `APPROVED`     | Decision Agent            | Claim has been accepted.                                 |
| `REJECTED`     | Decision Agent            | Claim has been denied.                                   |
| `ESCALATED`    | Any Agent / Manual Review | Sent to human for review due to complexity or suspicion. |

Example FLow:
RECEIVED
  → VALIDATED 
    → PENDING_INFO → VALIDATED (loop)
      → ASSESSED 
        → DECIDED 
          → APPROVED / REJECTED / ESCALATED

### TECH STACK TO USE:

- Database: Supabase
- Agent Framework: Agno
- LLM : Gemini API

