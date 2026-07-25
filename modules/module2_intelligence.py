from fastapi import APIRouter   # ✅ ADDED

router = APIRouter()            # ✅ ADDED


# ===============================
# YOUR ORIGINAL CODE BELOW (UNCHANGED)
# ===============================

@router.get("/intelligence/analyze/{company}")
def analyze_company(company: str):
    return {
        "company": company,
        "insight": f"{company} is growing rapidly in AI space"
    }


@router.post("/intelligence/score")
def score_lead(data: dict):
    score = 80 if data.get("status") == "contacted" else 50

    return {
        "company": data.get("company"),
        "score": score
    }