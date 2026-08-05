import unittest
import os
from database import ZeroCostDatabase
from provider_facility import FreeApiKeyFacility
from kernel import PersonalAgentOSKernel


class TestPersonalAgentOS(unittest.TestCase):

    def setUp(self):
        self.db = ZeroCostDatabase("/tmp/test_personal_os.db")
        self.facility = FreeApiKeyFacility()
        self.kernel = PersonalAgentOSKernel()

    def test_database_task_addition(self):
        task = self.db.add_task("Unit Test Task", "Alice SDR Worker", "High", "In Progress")
        self.assertTrue(task["id"].startswith("task_"))
        self.assertEqual(task["title"], "Unit Test Task")

        tasks = self.db.list_tasks()
        self.assertGreater(len(tasks), 0)

    def test_provider_status_reporting(self):
        status = self.facility.get_provider_status()
        self.assertIn("option_1_gemini_flash", status)
        self.assertIn("option_3_local_ai_engine", status)
        self.assertEqual(status["option_3_local_ai_engine"]["status"], "PRIMARY_ACTIVE")

    def test_ollama_health_check(self):
        health = self.facility.check_ollama_health()
        self.assertIn("endpoint", health)
        self.assertIn("online", health)

    def test_completion_generation(self):
        res = self.facility.generate_completion("Test goal execution")
        self.assertTrue(res["success"])
        self.assertEqual(res["cost"], "$0.00")
        self.assertIn("Option 3", res["provider"])

    def test_kernel_system_health(self):
        health = self.kernel.get_system_health()
        self.assertEqual(health["infrastructure_cost"], "$0.00 (100% Free Tier Stack)")
        self.assertEqual(len(health["active_digital_workers"]), 5)

    def test_kernel_agent_task_execution(self):
        res = self.kernel.execute_agent_task("Devin Software Engineer", "Audit web page code")
        self.assertTrue(res["success"])
        self.assertEqual(res["cost"], "$0.00")
        self.assertEqual(res["agent"], "Devin Software Engineer")


if __name__ == "__main__":
    unittest.main()
