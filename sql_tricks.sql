-- Use hashing and modulo operators to split dataset into training/validation. This is repeatable. Everytime we call this function, it return repeatable random splittingm .
SELECT date, a, b, target FROM `TABLE`
where MOD(ABS(FARM_FINGERPRINT(date)), 10) < 8  -- 80% training
;
SELECT date, a, b, target FROM `TABLE`
where MOD(ABS(FARM_FINGERPRINT(date)), 10) == 8  -- 10% validation
;
SELECT date, a, b, target FROM `TABLE`
where MOD(ABS(FARM_FINGERPRINT(date)), 10) == 9  -- 10% testing
;
