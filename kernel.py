import os
import json
import time
from typing import Dict, Any, List, Optional
from database import ZeroCostDatabase
from provider_facility import FreeApiKeyFacility


class PersonalAgentOSKernel:
    """
    Personal Agentic OS Core Kernel & Execution Engine.
    Orchestrates Digital Workers, Free API Key Routers, DAG Workflow Graphs,
    and $0-Cost Workspace Alerts (Notion & Slack).
    """

    def __init__(self):
        self.db = ZeroCostDatabase()
        self.providers = FreeApiKeyFacility()

    def get_system_health(self) -> Dict[str, Any]:
        return {
            "os_name": "Hermes Agentic Workspace (Project Anya)",
            "version": "3.5.0 Intelligence",
            "infrastructure_cost": "$0.00 (100% Free Tier Stack)",
            "database_status": "ONLINE (SQLite + JSON Local Mirror)",
            "providers": self.providers.get_provider_status(),
            "active_digital_workers": [
                {"name": "Hermes Chief Agent", "role": "Orchestrator & Technical Director", "status": "ACTIVE"},
                {"name": "Alice SDR Worker", "role": "Lead Generation & Outreach", "status": "ACTIVE"},
                {"name": "Sierra Support Worker", "role": "Customer CS & Order Mutations", "status": "ACTIVE"},
                {"name": "Devin Software Engineer", "role": "Autonomous Coding & Testing", "status": "ACTIVE"},
                {"name": "GitHub Developer Swarm Agent", "role": "GitHub Repos, Code Inspection & PR Reviews", "status": "ACTIVE"}
            ]
        }

    def execute_agent_task(self, agent_name: str, task_goal: str) -> Dict[str, Any]:
        """Executes a task for any assigned agent and logs to $0-cost database."""
        start_time = time.time()
        
        # Run goal through free provider facility
        completion = self.providers.generate_completion(task_goal, system_instruction=f"You are {agent_name} in Hermes Agentic Workspace.")
        exec_ms = round((time.time() - start_time) * 1000, 2)

        # Log task in Database
        task_record = self.db.add_task(
            title=f"[{agent_name}] {task_goal}",
            assignee=agent_name,
            priority="High",
            status="COMPLETED"
        )

        # Log run event
        run_record = self.db.record_agent_run(
            agent_name=agent_name,
            status="COMPLETED",
            prompt=task_goal,
            output=completion["text"],
            exec_ms=exec_ms
        )

        return {
            "success": True,
            "agent": agent_name,
            "goal": task_goal,
            "execution_ms": exec_ms,
            "provider_used": completion["provider"],
            "cost": "$0.00",
            "task_id": task_record["id"],
            "output": completion["text"]
        }


if __name__ == "__main__":
    kernel = PersonalAgentOSKernel()
    print("Health Status:", json.dumps(kernel.get_system_health(), indent=2))
    res = kernel.execute_agent_task("Alice SDR Worker", "Find 20 verified leads in Mumbai")
    print("Task Execution Result:", json.dumps(res, indent=2))
