from docling.document_converter import DocumentConverter


temp_db_chunk = []
source = "./uploaded_files/React_old_notes.pdf"
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())

result.document.export_to_markdown().append(temp_db_chunk)


# Impose limits on the document size

# You can limit the file size and number of pages which should be allowed to process per document:

# from pathlib import Path
# from docling.document_converter import DocumentConverter

# source = "https://arxiv.org/pdf/2408.09869"
# converter = DocumentConverter()
# result = converter.convert(source, max_num_pages=100, max_file_size=20971520)
