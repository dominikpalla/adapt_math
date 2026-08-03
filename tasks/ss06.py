"""
SŠ 06 — Úpravy algebraických výrazů (racionální, mocninné, odmocninové).

Zdroj: Overleaf `Andrea_příkladySŠ/Úpravy algebraických výrazů.tex`.
Zdroj duplikát (jiný layout, stejný obsah): `Zjednodušte algebraické výrazy2.tex` — přeskočen.

Extrahováno 2026-08-03. Podmínky (D) uvedeny v content_latex, aby student
viděl, na jaké omezené doméně pracujeme. Očekávaná hodnota je jen zjednodušený výraz.
"""


def _simp(idx, expr, expected, cl="C", domain=None):
    """Standardní 'zjednodušte' úloha s jedním mathlive výsledkem."""
    content = r"Zjednodušte výraz $" + expr + r"$"
    if domain:
        content += r" pro " + domain + "."
    else:
        content += "."
    return {
        "task_id": f"ss06_{idx:02d}",
        "content_latex": content,
        "results": [{
            "key": "vysledek", "label_latex": r"= ", "type": "mathlive",
            "expected": expected, "tolerance": 0.0,
        }],
        "cognitive_load": cl,
    }


TASKS = [
    _simp(1,
        r"\left(p + q - \frac{4pq}{p+q}\right) : \frac{1}{p^2 - q^2}",
        r"(p - q)^3", "C", r"$p \neq \pm q$"),
    _simp(2,
        r"\left(\frac{2x^2 - 4x + 2}{x^2 + 1} : \frac{6x - 6}{x^4 - 1}\right) : \frac{x + 1}{3}",
        r"(x - 1)^2", "C", r"$x \neq \pm 1$"),
    _simp(3,
        r"\left(v + \frac{u - v}{1 + uv}\right) : \left(1 - \frac{v(u - v)}{1 + uv}\right)",
        r"u", "C", r"$uv \neq -1$"),
    _simp(4,
        r"\frac{\frac{r + s}{r - s} - \frac{r - s}{r + s}}{1 - \frac{r^2 + s^2}{r^2 - s^2}}",
        r"-\frac{2r}{s}", "C", r"$r \neq \pm s,\ s \neq 0$"),
    _simp(5,
        r"\left(x + \frac{y - x}{1 + xy}\right) : \left(1 + \frac{x^2 - xy}{1 + xy}\right)",
        r"y", "C", r"$xy \neq -1$"),
    _simp(6,
        r"\frac{\frac{a}{b} + \frac{b}{a} - 1}{\frac{1}{a} + \frac{1}{b}} : \frac{a^3 - b^3}{a^2 - b^2}",
        r"\frac{a^2 + b^2 - ab}{a^2 + b^2 + ab}", "D", r"$a, b \neq 0,\ a \neq \pm b$"),
    _simp(7,
        r"\left(\frac{x - 3}{x + 3} + \frac{x + 3}{x - 3}\right) \cdot "
        r"\left(\frac{x^2 + 9}{6x} + 1\right) \cdot \frac{3x}{x^2 + 9}",
        r"\frac{x + 3}{x - 3}", "D", r"$x \neq 0,\ x \neq \pm 3$"),
    _simp(8,
        r"\left(\left(\frac{3}{x - y} + \frac{3x}{x^3 - y^3} \cdot \frac{x^2 + xy + y^2}{x + y}\right) : "
        r"\frac{2x + y}{x^2 + 2xy + y^2}\right) \cdot \frac{3}{x + y}",
        r"\frac{9}{x - y}", "E", r"$x \neq \pm y,\ x \neq -\frac{y}{2}$"),
    _simp(9,
        r"\left(\frac{a^3 - ab^2 + b^3}{(a - b)^3} - \frac{b}{a - b}\right) : "
        r"\left(\frac{a^2 - 2ab + 2b^2}{a^2 - ab + b^2} - \frac{b}{a}\right)",
        r"1", "E", r"$a \neq 0,\ a \neq b$"),
    _simp(10,
        r"\left(\left(1 - \frac{2}{1 - 3a}\right) \cdot \left(1 - \frac{9a - 9a^2}{3a + 1}\right)\right) : 2(1 - 9a^2)",
        r"-\frac{1}{2(1 + 3a)}", "D", r"$a \neq \pm \frac{1}{3}$"),
    _simp(11,
        r"\left(b^2 - \frac{a}{1 + \left(\frac{b - a}{a}\right)^{-1}} \cdot "
        r"\left(\frac{ab}{b - a} - a\right)\right) : \frac{a^2 + ab + b^2}{b}",
        r"b - a", "D", r"$a \neq b,\ b \neq 0$"),
    _simp(12,
        r"\frac{\frac{a + b}{a - b} - \frac{a - b}{a + b}}{1 - \frac{a^2 + b^2}{a^2 - b^2}} \cdot "
        r"\frac{2 - \frac{1 + b^2}{b}}{\frac{1}{b^2} - \frac{2}{b} + 1}",
        r"2a", "E", r"$a \neq \pm b,\ b \neq 0$"),
    _simp(13,
        r"\sqrt{a \cdot \sqrt[3]{b^{-1}}} : \sqrt[3]{b^2 \cdot \sqrt{a}} + \sqrt[6]{b} : b",
        r"\frac{1 + \sqrt[3]{a}}{\sqrt[6]{b^5}}", "E", r"$a > 0,\ b > 0$"),
    _simp(14,
        r"\sqrt[5]{\left(\frac{c^{1/2} \cdot c^{-1/3}}{c^{-5/6}}\right)^{-3}}",
        r"c^{-3/5}", "D", r"$c > 0$"),
    _simp(15,
        r"\frac{4^3 \cdot x^{-5} \cdot y^{-2}}{2^{-6} \cdot (x^3 + y^3)^{-2}} : (x^3 \cdot y^2)^{-2}",
        r"2^{12} \cdot (x^3 + y^3)^2 \cdot x y^2", "D", r"$x, y \neq 0,\ x \neq -y$"),
    _simp(16,
        r"\left(\left(a^3 \cdot b\right)^{\frac{1}{3}}\right)^{\frac{1}{2}} : "
        r"\left(\left(a^3 \cdot b^{-2}\right)^{\frac{1}{2}}\right)^{\frac{1}{3}}",
        r"\sqrt{b}", "D", r"$a > 0,\ b > 0$"),
    _simp(17,
        r"\sqrt{2ab} \cdot \sqrt[3]{4a^2 b^4} \cdot \sqrt[4]{8a^3 b^5} \cdot "
        r"\sqrt[6]{2a^5 b^6} \cdot \sqrt[12]{4a^2 b^8}",
        r"4a^2 b^4 \cdot \sqrt[12]{8a^{11} b^9}", "E", r"$a \ge 0,\ b \ge 0$"),
    _simp(18,
        r"\frac{\frac{x + y}{x - y} + \frac{x - y}{x + y}}{\frac{1}{(x + y)^2} + \frac{1}{(x - y)^2}}",
        r"x^2 - y^2", "D", r"$x \neq \pm y$"),
    _simp(19,
        r"\frac{\left(\frac{x}{y} + \frac{y}{x} - 1\right)\left(\frac{x}{y} + \frac{y}{x} + 1\right)(x^2 - y^2)}"
        r"{\frac{x^4}{y^2} - \frac{y^4}{x^2}}",
        r"1", "E", r"$x, y \neq 0,\ x \neq \pm y$"),
    _simp(20,
        r"\frac{1 - a^{-\frac{1}{2}}}{1 + a^{\frac{1}{2}}} - \frac{a^{\frac{1}{2}} + a^{-\frac{1}{2}}}{a - 1}",
        r"\frac{2}{1 - a}", "D", r"$a > 0,\ a \neq 1$"),
    _simp(21,
        r"\left((a + b)^{\frac{1}{2}} + a^{\frac{1}{2}} - b^{\frac{1}{2}}\right) \cdot "
        r"\left((a + b)^{\frac{1}{2}} - a^{\frac{1}{2}} + b^{\frac{1}{2}}\right)",
        r"2\sqrt{ab}", "D", r"$a > 0,\ b > 0$"),
    _simp(22,
        r"\left((a^{0{,}5} + b^{0{,}5})^2 - "
        r"\left(\frac{\sqrt{a} - \sqrt{b}}{a^{1{,}5} - b^{1{,}5}}\right)^{-1}\right) \cdot (ab)^{-0{,}5}",
        r"1", "E", r"$a > 0,\ b > 0,\ a \neq b$"),
    _simp(23,
        r"\left(\frac{a^{-\frac{2}{3}}}{b^{-1}} - \frac{b^{-1}}{a^{-\frac{2}{3}}}\right) : "
        r"\left(\frac{a^{-\frac{1}{3}}}{b^{-\frac{1}{2}}} - \frac{b^{-\frac{1}{2}}}{a^{-\frac{1}{3}}}\right) "
        r"- a^{\frac{1}{3}} \cdot b^{-\frac{1}{2}}",
        r"\frac{\sqrt{b}}{\sqrt[3]{a}}", "E", r"$a \neq 0,\ b > 0,\ b \neq \sqrt[3]{a^2}$"),
    _simp(24,
        r"\left(\frac{1}{\sqrt{y - 1}} + \frac{1}{\sqrt{y + 1}}\right) : "
        r"\left((\sqrt{y - 1})^{-1} - (\sqrt{y + 1})^{-1}\right)",
        r"y + \sqrt{y^2 - 1}", "D", r"$y > 1$"),
    _simp(25,
        r"\left(\sqrt{x} - \frac{1}{\sqrt{x}}\right) \cdot "
        r"\left(\frac{\sqrt{x} + 1}{\sqrt{x} - 1} + 4\sqrt{x} - \frac{\sqrt{x} - 1}{\sqrt{x} + 1}\right)",
        r"4x", "D", r"$x > 0,\ x \neq 1$"),
    _simp(26,
        r"\frac{(x + y)^{2a + 1}}{(u - v)^{2a - 1}} \cdot "
        r"\frac{(u - v)^{2a + 1}}{(x^2 - y^2)^{2a + 1}} \cdot "
        r"\frac{(x - y)^{2a + 2}}{(u - v)^2}",
        r"x - y", "E", r"$u \neq v,\ x \neq \pm y$"),
    _simp(27,
        r"\left(\frac{a\sqrt{a} + b\sqrt{b}}{\sqrt{a} + \sqrt{b}} - \sqrt{ab}\right) : (a - b) "
        r"+ \frac{2\sqrt{b}}{\sqrt{a} + \sqrt{b}}",
        r"1", "D", r"$a > 0,\ b > 0,\ a \neq b$"),
    _simp(28,
        # Poznámka: v .tex je typo `\left)` místo `\left(`; opraveno.
        r"\frac{a^4 - b^4}{a^2 \cdot b^2} : \left(\left(1 + \frac{b^2}{a^2}\right) \cdot "
        r"\left(1 - \frac{2a}{b} + \frac{a^2}{b^2}\right)\right)",
        r"\frac{a + b}{a - b}", "E", r"$a, b \neq 0,\ a \neq b$"),
    _simp(29,
        r"\frac{\sqrt{2a} - \frac{2a}{a + \sqrt{2a}}}{\frac{\sqrt{2a} - 2}{a - 2}}",
        r"a", "D", r"$a > 0,\ a \neq 2,\ a \neq \sqrt{2}$"),
    _simp(30,
        r"\left(\left(\frac{n + 2}{n - 2}\right)^3 : \frac{n^3 + 4n^2 + 4n}{3n^2 - 12n + 12}\right) \cdot \frac{n}{3}",
        r"\frac{n + 2}{n - 2}", "D", r"$n \neq \pm 2$"),
    _simp(31,
        r"\left(1 + \frac{\frac{a + b}{a}}{\frac{a - 3b}{a}}\right) : "
        r"\left(1 - 3 \cdot \frac{\frac{a + b}{a}}{\frac{a - 3b}{a}}\right)",
        r"\frac{b - a}{a + 3b}", "D", r"$a \neq 0,\ a \neq \pm 3b$"),
    _simp(32,
        r"2u - \left(\frac{2u - 3}{u + 1} - \frac{u + 1}{2 - 2u} - \frac{u^2 + 3}{2u^2 - 2}\right) \cdot "
        r"\frac{u^3 + 1}{u^2 - u}",
        r"\frac{2(u - 1)}{u}", "E", r"$u \neq 0,\ u \neq \pm 1$"),
    _simp(33,
        r"\left(\frac{x^{-\frac{2}{3}}}{y^{-1}} - \frac{y^{-1}}{x^{-\frac{2}{3}}}\right) : "
        r"\left(\frac{x^{-\frac{1}{3}}}{y^{-\frac{1}{2}}} - \frac{y^{-\frac{1}{2}}}{x^{-\frac{1}{3}}}\right)",
        r"\frac{\sqrt[3]{x^2} + y}{\sqrt[6]{x^2 \cdot y^3}}", "E", r"$x > 0,\ y > 0$"),
    _simp(34,
        r"\left(\sqrt{a} + \frac{b - \sqrt{ab}}{\sqrt{a} + \sqrt{b}}\right) : "
        r"\left(\frac{a + b}{\sqrt{ab}} - \frac{b}{\sqrt{ab}} - \frac{a}{\sqrt{ab} + b}\right)",
        r"\frac{a + b}{\sqrt{a}}", "E", r"$a > 0,\ b > 0$"),
    _simp(35,
        r"x^3 \cdot \sqrt[3]{x \cdot \sqrt{x}} \cdot "
        r"\left(\frac{(\sqrt[4]{x} + \sqrt[4]{y})^2 + (\sqrt[4]{x} - \sqrt[4]{y})^2}{x + \sqrt{xy}}\right)^5",
        r"32x", "E", r"$x > 0,\ y > 0$"),
    _simp(36,
        r"\sqrt{\frac{(1 + a) \cdot \sqrt[3]{1 + a}}{3a}} \cdot \sqrt[3]{\frac{\sqrt{3}}{9 + 18a^{-1} + 9a^{-2}}}",
        r"\frac{\sqrt[6]{a}}{3}", "E", r"$a > 0$"),
    _simp(37,
        r"\left(x \cdot \sqrt[6]{\frac{y^2}{x}} + y \cdot \sqrt[6]{\frac{x^2}{y}}\right) \cdot "
        r"\frac{\sqrt[6]{xy}}{\sqrt{x} + \sqrt{y}}",
        r"\sqrt{xy}", "E", r"$x > 0,\ y > 0$"),
    _simp(38,
        r"\left(1 + \frac{1 + \frac{1 - x^2}{1 + x^2}}{1 - \frac{1 - x^2}{1 + x^2}}\right) \cdot "
        r"\frac{1}{1 + \frac{1}{x^2}}",
        r"1", "D", r"$x \neq 0$"),
    _simp(39,
        r"\frac{\frac{1 - x}{1 - x + x^2} + \frac{1 + x}{1 + x + x^2}}"
        r"{\frac{1 + x}{1 + x + x^2} - \frac{1 - x}{1 - x + x^2}}",
        r"x^{-3}", "E", r"$x \neq 0$"),
    _simp(40,
        r"\left((a^{\frac{1}{3}} - x^{\frac{1}{3}})^{-1} \cdot (a - x) - "
        r"\frac{a + x}{a^{\frac{1}{3}} + x^{\frac{1}{3}}}\right) \cdot 2^{-1} \cdot (ax)^{-\frac{1}{3}}",
        r"1", "E", r"$a \neq 0,\ x \neq \pm a$"),
    _simp(41,
        r"\left(\frac{1 + \sqrt{x}}{\sqrt{1 + x}} - \frac{\sqrt{1 + x}}{1 + \sqrt{x}}\right)^{-2} - "
        r"\left(\frac{1 - \sqrt{x}}{\sqrt{1 + x}} - \frac{\sqrt{1 + x}}{1 - \sqrt{x}}\right)^{-2}",
        r"\frac{(1 + x)\sqrt{x}}{x}", "E", r"$x > 0,\ x \neq 1$"),
    _simp(42,
        r"\frac{\frac{2x}{\sqrt{x + 1}} + \sqrt{x - 1}}{1 + \sqrt{\frac{x - 1}{x + 1}}} \cdot "
        r"\frac{2x}{(x + 1)\sqrt{x + 1} - (x - 1)\sqrt{x - 1}}",
        r"x", "E", r"$x \ge 1$"),
    _simp(43,
        r"\frac{a\left(\frac{\sqrt{a} + \sqrt{b}}{2b\sqrt{a}}\right)^{-1} + b\left(\frac{\sqrt{a} + \sqrt{b}}{2a\sqrt{b}}\right)^{-1}}"
        r"{\left(\frac{a + \sqrt{ab}}{2ab}\right)^{-1} + \left(\frac{b + \sqrt{ab}}{2ab}\right)^{-1}}",
        r"\sqrt{ab}", "E", r"$a > 0,\ b > 0$"),
]
