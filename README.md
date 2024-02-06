# Social Media Network Ads Analytics Project

## Introduction

This project undertakes a detailed analysis of the 'Social Media Network Ads' dataset from Kaggle, focusing on the impact of user demographics on social media advertisement effectiveness. The primary objective is to identify demographic factors, such as age and income, that influence the likelihood of purchase conversions and to determine which segments are most responsive to ads. This insight is crucial for businesses looking to optimize their social media marketing strategies and improve their return on advertising spend.

For the purposes of this analysis, we operate under the assumption that the product or service advertised is universally appealing across all age groups and income demographics. This assumption is critical as it allows for a fair assessment and comparison of purchase rates, ensuring that our insights reflect the effectiveness of ad reach and engagement rather than the varying appeal of the product itself.

## Research Question

The guiding research question for this project is:

**"How do demographic factors such as age and income influence the likelihood of a purchase following exposure to social media advertisements, and which demographic segments should be targeted to maximize return on advertising spend?"**

This question directs the analytical efforts towards uncovering actionable trends and relationships within the data.

## Data Source

The dataset used in this analysis is available on Kaggle and can be found at the following link:

- [Social Media Network Ads Dataset](https://www.kaggle.com/datasets/asmitameghrajchaskar/social-media-network-ads?rvi=1)

It includes key demographic information about users, including whether they made a purchase after viewing a social media ad.

## Methodology

Using Python for data analysis, we processed and analyzed the dataset to calculate the purchase rates across different demographics, income groups, and age brackets. The analysis involved:

- Cleaning and preprocessing the data.
- Segmenting users into meaningful groups based on age and income.
- Calculating the purchase rates for each segment.
- Identifying patterns and trends in the data.

Next, we will use Microsoft Power BI to visualize the data and make insights.

## Findings and Insights

The analysis of the 'Social Media Network Ads' dataset led to some compelling insights, particularly regarding the purchase rates across different age groups for both males and females. The visuals below depict the average purchase rate by age group for each gender:

- For females, the highest purchase rate was observed in the 50-64 age group, suggesting that women in this age bracket are the most responsive to social media ads.
- In contrast, the purchase rate for females in the 18-29 and 30-49 age groups was significantly lower.

![Average Purchase Rate by AgeGroup for Females](/output/agegroup_female.png)
*Figure 1: Purchase Rates Among Females by Age Group*

- For males, the trend showed a similar pattern, with the 50-64 age group having the highest purchase rate, indicating a strong responsiveness in this demographic as well.

![Average Purchase Rate by AgeGroup for Males](/output/agegroup_male.png)
*Figure 2: Purchase Rates Among Males by Age Group*

These trends provide a clear direction for advertisers; targeting the 50-64 age group could potentially yield higher conversion rates. However, it's also essential to consider the overall marketing strategy, product type, and the specific interests of the target demographic when tailoring ad campaigns.

Furthering our analysis into the 'Social Media Network Ads' dataset, we examined purchase rates across income brackets for males and females. Here are the summarized insights:

- **Females**: Women within the `$100,000+` income bracket exhibited the highest purchase rates, indicating their greater likelihood of responding to social media ads. 
- **Males**: Similarly, men in the `$100,000+` income bracket demonstrated the highest purchase rates, suggesting that targeting this demographic could be particularly profitable.

These findings underline the significance of income as a factor in advertising effectiveness. The detailed visualizations included below provide a clearer understanding of these trends:

![Average Purchase Rate by Income Bracket for Females](/output/income_female.png)
*Figure 3: Purchase Rates Among Females by Income Bracket*

![Average Purchase Rate by Income Bracket for Males](/output/income_male.png)
*Figure 4: Purchase Rates Among Males by Income Bracket*


## Conclusion: Strategic Advertising Insights

The investigation into social media ad effectiveness based on the 'Social Media Network Ads' dataset provides critical insights for strategic advertising. By analyzing user demographics and purchase rates, we identify key opportunities for businesses to enhance their ad targeting.

From the age-based analysis, we found that individuals in the 50-64 age bracket, regardless of gender, exhibit the highest purchase rates. This suggests that advertising campaigns targeting this age group are likely to be more effective, especially for products with universal appeal.

In terms of income, individuals in the `$100,000+` bracket show a strong propensity to purchase, making them prime targets for premium and luxury product ads.

Combining these insights with external data on social media platform usage by different demographics, we can conclude the following for ad placement:

- **Facebook and YouTube** show high usage across all age groups and income brackets, suggesting these platforms are valuable for widespread reach.
- **Instagram and Snapchat** are more popular with younger audiences, which may be more suitable for products aimed at the 18-29 age group.
- **LinkedIn** appears to be an effective platform for targeting professionals, especially those in higher income brackets.

Given these findings, businesses should consider a diversified ad strategy that leverages Facebook and YouTube for broad reach campaigns. At the same time, Instagram and Snapchat can be utilized for targeting younger demographics. For high-income professionals, LinkedIn may yield the best return on investment.

![Social Media Usage by Age](/output/social_media_age.png)
*Figure 5: Social Media Usage by Age*

![Social Media Usage by Income](/output/social_media_income.png)
*Figure 6: Social Media Usage by Income*

Ultimately, the choice of platform should align with the specific marketing goals, targeted demographics, and product type. Advertisers must continually adapt to the evolving social media landscape to capture the attention of their desired audience effectively.

---

The data for platform usage was referenced from Pew Research Center's studies on social media use found here:
- [Social Media Use by Age and Income](https://www.pewresearch.org/internet/fact-sheet/social-media/?tabId=tab-5b319c90-7363-4881-8e6f-f98925683a2f)

