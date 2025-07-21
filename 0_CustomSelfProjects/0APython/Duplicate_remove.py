

VALUES = ['a','b','c','d','d','e','f','g','h','h','i','i','i','i']

remove_duplicates = []
duplicate_values = []

for value in VALUES:
    if value not in remove_duplicates:
        remove_duplicates.append(value)
    else:
        if value not in duplicate_values:
            duplicate_values.append(value)




print(f"Original values: {VALUES}")
print(f"Duplicate values: {duplicate_values}")
print(f"Unique values: {remove_duplicates}")














# def remove_duplicates(values):
#     """
#     Remove duplicates from a list while preserving order.   
#     """
#     seen = set()
#     unique_values = []
#     for value in values:
#         if value not in seen:
#             seen.add(value)
#             unique_values.append(value)
#     return unique_values
# if __name__ == "__main__":
#     unique_values = remove_duplicates(VALUES)
#     print(f"Original values: {VALUES}") 
#     print(f"Unique values: {unique_values}")
#     # Output:
#     # Original values: ['a', 'b', 'c', 'd', 'd', 'e', 'f', 'g', 'h', 'h', 'i', 'i', 'i', 'i']
#     # Unique values: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# # This code defines a function to remove duplicates from a list while preserving the order of elements.
# # It uses a set to track seen values and a list to store unique values. The function iterates through the input list, adding each value to the set and the unique list only if it hasn't been seen before.
# # The main block demonstrates how to use this function with a sample list of values.
# # The output shows the original list and the list with duplicates removed.
# # This approach is efficient and maintains the order of the first occurrences of each value.
# # This code is useful for cleaning up lists where duplicates may cause issues, such as in data processing or analysis tasks.
# #         html_output += f"<div style='margin-left:20px'>{item.content}</div>"
# #         html_output += "</div>"
# #         html_output += "<div style='margin-bottom:20px'>"
# #         html_output += f"<div style='font-weight:bold'>{agent_name}:</div>"
# #             full_response.append(item.content)

# #                 else:
# #                     full_response.append(str(item))
# #                     html_output += f"<div style='margin-left:20px; white-space:pre-wrap'>{item}</div>"
# #   #         html_output += "</div>"   #         html_output += "</div>"
# # 
# #         # Combine all parts of the response   
# #         full_response_str = "".join(full_response)
# #         html_output += f"<div style='margin-left:20px; white-space:pre-wrap'>{full_response_str}</div>"
# #         html_output += "</div>"
# #         print(html_output)
# #         # Print the final response
# #         print(f"\n--- {agent_name} Response ---\n{full_response_str}")
# #
# #             first_chunk = False







