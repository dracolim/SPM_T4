import unittest

from app2 import Skill, JobRole, LearningJourney, LearningJourneySkill, LearningJourneyCourse, Staff, Registration

class TestJobRole(unittest.TestCase):
    def test_to_dict(self):
        jr1 = JobRole(job_role_name="Analyst", job_role_description="Analyse work", job_role_deleted= False)
        self.assertEqual(jr1.to_dict(), {
            'job_role_id': None, 
            'job_role_name': "Analyst",
            'job_role_description': 'Analyse work',
            'job_role_deleted': False
            }
        )

class TestSkill(unittest.TestCase):
    def test_to_dict(self):
        s1 = Skill(skill_name="JavaScript", skill_description="JavaScript is a lightweight interpreted programming language.", skill_deleted= False)
        self.assertEqual(s1.to_dict(), {
            'skill_id': None, 
            'skill_name': "JavaScript",
            'skill_description': 'JavaScript is a lightweight interpreted programming language.',
            'skill_deleted': False
            }
        )

    def test_update_skill(self):
        s1 = Skill(skill_name="JavaScript", skill_description="JavaScript is a lightweight interpreted programming language.", skill_deleted= False)
        self.assertEqual(s1.skill_name, "JavaScript")
        self.assertEqual(s1.skill_description, "JavaScript is a lightweight interpreted programming language.")
        s1.update_skill("UpdatedSkill", "UpdatedSkillDescription")
        self.assertEqual(s1.skill_name, "UpdatedSkill")
        self.assertEqual(s1.skill_description, "UpdatedSkillDescription")
        

class TestLearningJourneySkill(unittest.TestCase):
    def test_to_dict(self):
        ljs1 = LearningJourneySkill(learning_journey_id=1, skill_id=3)
        
        self.assertEqual(ljs1.to_dict(), {
            'learning_journey_id': 1,
            'skill_id': 3,
            }
        )

class TestLearningJourneyCourse(unittest.TestCase):
    def test_to_dict(self):
        ljc1 = LearningJourneyCourse(learning_journey_id=1, course_id="COR002")
        self.assertEqual(ljc1.to_dict(), {
            'learning_journey_id': 1, 
            'course_id': "COR002",
            }
        )

class TestStaff(unittest.TestCase):
    def test_to_dict(self):
        staff1 = Staff(staff_Fname="Lucas", staff_Lname="Lee",department="HR", email="Lucas.Lee@allinone.com.sg",role=1)
        self.assertEqual(staff1.to_dict(), {
            'staff_id': None,
            'staff_Fname': "Lucas", 
            'staff_Lname': "Lee",
            'department': "HR",
            'email': "Lucas.Lee@allinone.com.sg",
            'role': 1,
            }
        )

class TestRegistration(unittest.TestCase):
    def test_to_dict(self):
        r1 = Registration(course_id="COR002",staff_id=150288, reg_status="Registered",completion_status='Completed')
        self.assertEqual(r1.to_dict(), {
            'reg_id': None,
            'course_id': "COR002", 
            'staff_id': 150288,
            'reg_status': "Registered",
            'completion_status': "Completed",
            }
        )

    
class TestLearningJourney(unittest.TestCase):
    def test_to_dict(self):
        lj1 = LearningJourney(staff_id=1, job_role_id=1)
        print(f"ljs1.to_dict(): {lj1.to_dict()}")
        self.assertEqual(lj1.to_dict(), {
            'learning_journey_id': None,
            'staff_id': 1,
            'job_role_id': 1,
            'learning_journey_deleted': None
        })

    # def test_create_learning_journey(self):
    #     # role = Role(name="Staff")
    #     # job_role = JobRole(job_role_name="Analyst", job_role_description="Analyse work", job_role_deleted= False)
    #     # print(job_role.to_dict())
    #     # staff = Staff(staff_Fname="Jane", staff_Lname="Smith", department="Cardiac", email="janesmith@gmail.com", role=role.id)
    #     ljc1 = LearningJourney(staff_id=1, job_role_id=1)
    #     # ljc2 = LearningJourney(staff_id=staff.staff_id, job_role_id=job_role.job_role_id)
    #     # learningJourneyList = LearningJourney.query.all()
        
    #     # items = [learningJourney.to_dict()
    #     #             for learningJourney in learningJourneyList]
    #     print("sss:",ljc1.to_dict())
    #     # print()
    #     # self.assertEqual(ljc1.to_dict(), {
    #     #     'learning_journey_id': 1, 
    #     #     'course_id': "COR002",
    #     #     }
    #     # )

    #     self.assertEqual(ljc1.to_dict(), {
    #         'learning_journey_id': None,
    #         'staff_id': 1,
    #         'job_role_id': 1
    #     })


if __name__ == "__main__":
    unittest.main()