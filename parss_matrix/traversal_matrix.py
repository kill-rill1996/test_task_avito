import aiohttp


async def get_url_data(url: str) -> str | None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # print(resp.status)
            return await resp.text()


def pars_text_matrix(matrix_text: str) -> list[list[int]]:
    result = []
    for line in matrix_text.split('\n'):
        if line.startswith('|'):
            number_list = [int(new_line.strip()) for new_line in line.split('|')[1:-1]]
            result.append(number_list)
    return result


def traverse_matrix(matrix: list[list[int]], output: list[int] = None) -> list[int]:
    if output is None:
        output = []

    if not len(matrix):
        return output

    matrix = list(zip(*matrix[::-1]))
    output.extend(matrix[0][::-1])
    traverse_matrix(matrix[1:], output)


async def get_matrix(url: str) -> list[int]:
    output = []
    text = await get_url_data(url)
    traverse_matrix(pars_text_matrix(text))
    return output


