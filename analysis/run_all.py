import unittest
from fractions import Fraction as F

def frontier(rows, cost=True):
    vectors=[(F(str(c)), -F(str(f)), -b) if cost else (F(str(c)), -F(str(f))) for b,c,f in rows]
    return [rows[i][0] for i,v in enumerate(vectors) if not any(all(a>=b for a,b in zip(w,v)) and any(a>b for a,b in zip(w,v)) for w in vectors)]

def utility(p,r,c):
    if min(p,r,c)<0 or p+r+c!=1: raise ValueError('Invalid weights')
    return F(871,1000)*p+F(774,1000)*r-F(23,30)*c

def feasibility(value,budget):
    return 'unknown' if value is None else 'feasible' if value<=budget else 'infeasible'

class Tests(unittest.TestCase):
    def test_pareto(self):
        rows=[(350,.651,.092),(700,.687,.076),(1400,.695,.087),(2800,.697,.081)]
        self.assertEqual(frontier(rows),[350,700,1400,2800]); self.assertEqual(frontier(rows,False),[700,2800])
    def test_boundaries(self):
        for a,p in [(F(774,1000),False),(F(871,1000),True)]:
            c=a/(a+F(23,30)); self.assertEqual(utility(1-c if p else F(0),F(0) if p else 1-c,c),0)
    def test_grid(self):
        lo=F(774,1000)/(F(774,1000)+F(23,30)); hi=F(871,1000)/(F(871,1000)+F(23,30))
        for c in range(101):
            for p in range(101-c):
                w=F(c,100); u=utility(F(p,100),F(100-c-p,100),w)
                if w<lo: self.assertGreater(u,0)
                if w>hi: self.assertLess(u,0)
    def test_constraints(self):
        for budget,expected in [(30,('infeasible','infeasible')),(40,('feasible','infeasible')),(50,('feasible','infeasible')),(60,('feasible','feasible')),(70,('feasible','feasible'))]:
            self.assertEqual((feasibility(37,budget),feasibility(60,budget)),expected)
        self.assertEqual(feasibility(None,50),'unknown')
    def test_effects(self):
        self.assertEqual(round((60-37)/37*100,2),62.16)
        self.assertEqual(round((43.34-27.86)/43.34*100,2),35.72)
        self.assertEqual(round(47.68-38.97,2),8.71)
    def test_invalid_weights(self):
        with self.assertRaises(ValueError): utility(F(1),F(1),F(0))
if __name__=='__main__': unittest.main(verbosity=2)
