import pandas as pd
import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 3:
    print("Usage: python script_name.py <abricate_output.txt> <output_file.csv>")
    sys.exit(1)

# Load the input arguments
abricate_output_file = sys.argv[1]
output_file = sys.argv[2]

# Load the abricate output
abricate_df = pd.read_csv(abricate_output_file, sep='\t')

# Clean up column names by stripping any leading/trailing whitespace
abricate_df.columns = abricate_df.columns.str.strip()

# Inspect the columns to verify their names
print(f"Columns in the input file: {abricate_df.columns.tolist()}")

# Ensure the column names match what we need
abricate_filtered = abricate_df[['#FILE', 'SEQUENCE', 'GENE', '%COVERAGE', '%IDENTITY']]

# Group by contig and count the number of unique virulence genes
contig_ranking = abricate_filtered.groupby('SEQUENCE').agg(
    num_virulence_genes=('GENE', 'nunique'),
    avg_identity=('%IDENTITY', 'mean'),
    avg_coverage=('%COVERAGE', 'mean')
).reset_index()

# Sort by number of virulence genes and then by average identity or coverage if needed
contig_ranking = contig_ranking.sort_values(by=['num_virulence_genes', 'avg_identity'], ascending=False)

# Save the ranked output to the specified file
contig_ranking.to_csv(output_file, index=False)

print(f"Ranking completed. Results saved to {output_file}")