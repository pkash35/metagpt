import asyncio
import fire
import streamlit as st

from metagpt.roles import (
    Architect,
    Engineer,
    ProductManager,
    ProjectManager,
    QaEngineer,
)
from metagpt.team import Team


async def startup(
    idea: str,
    investment: float = 2.0,
    n_round: int = 5,
    code_review: bool = False,
    run_tests: bool = False,
    implement: bool = True,
):
    """Run a startup. Be a boss."""
    company = Team()
    company.hire(
        [
            ProductManager(),
            Architect(),
            ProjectManager(),
        ]
    )

    # if implement or code_review
    if implement or code_review:
        # developing features: implement the idea
        company.hire([Engineer(n_borg=5, use_code_review=code_review)])

    if run_tests:
        # developing features: run tests on the spot and identify bugs
        # (bug fixing capability comes soon!)
        company.hire([QaEngineer()])

    company.invest(investment)
    company.start_project(idea)
    await company.run(n_round=n_round)

def run_startup(idea, investment=2.0, n_round=5, code_review=True, run_tests=False, implement=True):
    asyncio.run(startup(idea, investment, n_round, code_review, run_tests, implement))

def main(
    idea: str,
    investment: float = 2.0,
    n_round: int = 5,
    code_review: bool = True,
    run_tests: bool = False,
    implement: bool = True,
):
    """
    We are a software startup comprised of AI. By investing in us,
    you are empowering a future filled with limitless possibilities.
    :param idea: Your innovative idea, such as "Creating a snake game."
    :param investment: As an investor, you have the opportunity to contribute
    a certain dollar amount to this AI company.
    :param n_round:
    :param code_review: Whether to use code review.
    :return:
    """
    asyncio.run(startup(idea, investment, n_round, code_review, run_tests, implement))


def main():
    st.title("AI Startup Simulator")

    # User input using Streamlit widgets
    idea = st.text_input("Enter your startup idea:")
    investment = st.slider("Investment amount:", min_value=1.0, max_value=10.0, value=3.0)
    n_round = st.number_input("Number of funding rounds:", min_value=1, value=5)
    code_review = st.checkbox("Use code review")
    run_tests = st.checkbox("Run tests")
    implement = st.checkbox("Implement features")

    # Run the startup function when the user clicks the "Run Startup" button
    if st.button("Run Startup"):
        # Display a loading message while the startup is running
        with st.spinner("Running startup..."):
            # Call the original startup function from the startup script
            run_startup(idea=idea, investment=investment, n_round=n_round, code_review=code_review, run_tests=run_tests, implement=implement)


if __name__ == "__main__":
    main()
    #fire.Fire(main)
