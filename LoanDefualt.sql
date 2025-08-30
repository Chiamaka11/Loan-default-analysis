SELECT 
    [Age],
    [Income],
    [LoanAmount],
    [CreditScore],
    [MonthsEmployed],
    [NumCreditLines],
    [InterestRate],
    [LoanTerm],
    [DTIRatio],
    [Education],
    [EmploymentType],
    [MaritalStatus],
    [HasMortgage],
    [HasDependents],
    [LoanPurpose],
    [HasCoSigner],
    [Default],
    -- Calculated columns
    (LoanAmount / LoanTerm) AS Installment_per_Month,
    ROUND((MonthsEmployed / 12.0), 2) AS YearsEmployed,
    ROUND(((LoanAmount / LoanTerm) / Income), 2) AS Installment_to_IncomeRatio,
    ROUND(((MonthsEmployed / 12.0) / Age), 2) AS EmployabilityStability
FROM Loan_default;
